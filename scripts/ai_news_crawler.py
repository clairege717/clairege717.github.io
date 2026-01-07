#!/usr/bin/env python3
"""
AI News Crawler - 从多个资讯网站爬取AI热门资讯
支持的网站：TechCrunch、36氪、钛媒体、机器之心、InfoQ

使用方式：
    python scripts/ai_news_crawler.py --days 1 --output DailyAI
"""

import os
import re
import sys
import json
import time
import hashlib
import feedparser
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from typing import List, Optional
from urllib.parse import urljoin, quote

import requests
from bs4 import BeautifulSoup


@dataclass
class NewsItem:
    """新闻条目数据类"""
    title: str
    url: str
    publish_time: str
    source: str
    summary: str = ""
    
    def to_dict(self):
        return asdict(self)


class BaseCrawler:
    """爬虫基类"""
    
    def __init__(self, source_name: str, base_url: str):
        self.source_name = source_name
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
    
    def fetch_page(self, url: str, retries: int = 3, timeout: int = 30) -> Optional[str]:
        """获取页面内容，带重试机制"""
        for attempt in range(retries):
            try:
                response = self.session.get(url, timeout=timeout)
                # 处理重定向
                if response.status_code in (301, 302):
                    url = response.headers.get('Location', url)
                    response = self.session.get(url, timeout=timeout)
                
                response.raise_for_status()
                return response.text
            except Exception as e:
                print(f"  [{self.source_name}] 获取页面失败 (尝试 {attempt + 1}/{retries}): {url}")
                if attempt < retries - 1:
                    time.sleep(2 + attempt)
        return None
    
    def crawl(self, days: int = 1) -> List[NewsItem]:
        """爬取新闻，子类需实现此方法"""
        raise NotImplementedError


class RSSCrawler(BaseCrawler):
    """RSS 订阅源爬虫基类"""
    
    def __init__(self, source_name: str, rss_url: str):
        super().__init__(source_name, "")
        self.rss_url = rss_url
    
    def crawl(self, days: int = 1) -> List[NewsItem]:
        """通过 RSS 爬取新闻"""
        news_list = []
        yesterday = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        try:
            feed = feedparser.parse(self.rss_url)
            
            for entry in feed.entries[:20]:
                try:
                    title = entry.get('title', '').strip()
                    url = entry.get('link', '')
                    if not title or not url:
                        continue
                    
                    # 获取发布时间
                    if hasattr(entry, 'published'):
                        time_str = entry.published
                    elif hasattr(entry, 'updated'):
                        time_str = entry.updated
                    else:
                        time_str = ''
                    
                    publish_time = self._parse_publish_time(time_str, yesterday)
                    
                    # 只保留昨天的新闻
                    if publish_time != yesterday:
                        continue
                    
                    # 获取摘要
                    summary = ''
                    if hasattr(entry, 'summary'):
                        summary = entry.summary
                        # 去除HTML标签
                        summary = re.sub(r'<[^>]+>', '', summary)
                        summary = summary[:200]
                    elif hasattr(entry, 'description'):
                        summary = entry.description
                        summary = re.sub(r'<[^>]+>', '', summary)
                        summary = summary[:200]
                    
                    news_list.append(NewsItem(
                        title=title,
                        url=url,
                        publish_time=publish_time,
                        source=self.source_name,
                        summary=summary
                    ))
                except Exception as e:
                    print(f"  [{self.source_name}] 解析RSS条目失败: {e}")
                    continue
            
            print(f"  [{self.source_name}] 通过RSS获取到 {len(news_list)} 条新闻")
        except Exception as e:
            print(f"  [{self.source_name}] RSS解析失败: {e}")
        
        return news_list
    
    def _parse_publish_time(self, time_str: str, default: str) -> str:
        """解析发布时间"""
        if not time_str:
            return default
        
        try:
            # 尝试多种日期格式
            formats = [
                '%Y-%m-%dT%H:%M:%S%z',
                '%Y-%m-%dT%H:%M:%SZ',
                '%Y-%m-%d %H:%M:%S',
                '%Y-%m-%d',
                '%d %b %Y %H:%M %Z',
            ]
            
            for fmt in formats:
                try:
                    dt = datetime.strptime(time_str[:19], fmt.split('T')[0].split()[0])
                    return dt.strftime('%Y-%m-%d')
                except:
                    continue
        except:
            pass
        
        return default


class TechCrunchCrawler(BaseCrawler):
    """TechCrunch AI 新闻爬虫"""
    
    def __init__(self):
        super().__init__("TechCrunch", "https://techcrunch.com")
        self.rss_url = "https://techcrunch.com/category/artificial-intelligence/feed/"
    
    def crawl(self, days: int = 1) -> List[NewsItem]:
        """爬取 TechCrunch AI 相关新闻"""
        news_list = []
        yesterday = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        # 尝试 RSS 方式
        try:
            feed = feedparser.parse(self.rss_url)
            
            for entry in feed.entries[:15]:
                try:
                    title = entry.get('title', '').strip()
                    url = entry.get('link', '')
                    if not title or not url:
                        continue
                    
                    # 解析时间
                    publish_time = self._parse_time(entry.get('published', ''), yesterday)
                    
                    # 只保留昨天的新闻
                    if publish_time != yesterday:
                        continue
                    
                    # 清理摘要中的HTML
                    summary = entry.get('summary', '')
                    summary = re.sub(r'<[^>]+>', '', summary)
                    
                    news_list.append(NewsItem(
                        title=title,
                        url=url,
                        publish_time=publish_time,
                        source="TechCrunch",
                        summary=summary[:200]
                    ))
                except Exception as e:
                    print(f"  [TechCrunch] 解析失败: {e}")
                    continue
            
            if news_list:
                print(f"  [TechCrunch] 获取到 {len(news_list)} 条新闻")
                return news_list
        except Exception as e:
            print(f"  [TechCrunch] RSS失败: {e}")
        
        # 备用：网页爬取
        url = "https://techcrunch.com/category/artificial-intelligence/"
        html = self.fetch_page(url)
        
        if not html:
            return news_list
        
        soup = BeautifulSoup(html, 'lxml')
        
        articles = soup.select('div.wp-block-outer-artificial-intelligence-article-card-outer article')
        
        for article in articles[:10]:
            try:
                title_elem = article.select_one('h2.entry-title a')
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True)
                url = title_elem.get('href', '')
                
                time_elem = article.select_one('time')
                publish_time = yesterday
                if time_elem:
                    dt = time_elem.get('datetime', '')[:10]
                    if dt:
                        publish_time = dt
                
                if publish_time != yesterday:
                    continue
                
                summary_elem = article.select_one('p.excerpt')
                summary = summary_elem.get_text(strip=True) if summary_elem else ""
                
                news_list.append(NewsItem(
                    title=title,
                    url=url,
                    publish_time=publish_time,
                    source="TechCrunch",
                    summary=summary[:200]
                ))
            except Exception as e:
                continue
        
        print(f"  [TechCrunch] 获取到 {len(news_list)} 条新闻")
        return news_list
    
    def _parse_time(self, time_str: str, default: str) -> str:
        """解析时间字符串（支持多种格式）"""
        if not time_str:
            return default
        try:
            # RFC 2822 格式: Mon, 28 Dec 2025 00:00:00 GMT
            from email.utils import parsedate_to_datetime
            dt = parsedate_to_datetime(time_str)
            return dt.strftime('%Y-%m-%d')
        except:
            pass
        try:
            # ISO 格式
            if 'T' in time_str:
                dt = datetime.fromisoformat(time_str.replace('Z', '+00:00').replace('+00:00', ''))
                return dt.strftime('%Y-%m-%d')
        except:
            pass
        try:
            # 简单日期格式
            dt = datetime.strptime(time_str[:10], '%Y-%m-%d')
            return dt.strftime('%Y-%m-%d')
        except:
            pass
        return default


class Kr36Crawler(BaseCrawler):
    """36氪 AI 新闻爬虫"""
    
    def __init__(self):
        super().__init__("36氪", "https://36kr.com")
    
    def crawl(self, days: int = 1) -> List[NewsItem]:
        """爬取 36氪 AI 相关新闻"""
        news_list = []
        yesterday = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        # 尝试搜索方式获取AI新闻
        search_urls = [
            f"https://36kr.com/api/search/meta?keyword={quote('AI')}&page=1",
            f"https://36kr.com/api/search/meta?keyword={quote('人工智能')}&page=1",
        ]
        
        for api_url in search_urls:
            html = self.fetch_page(api_url)
            if not html:
                continue
            
            try:
                data = json.loads(html)
                items = data.get('data', {}).get('items', [])
                
                for item in items[:15]:
                    title = item.get('title', '').strip()
                    url = item.get('link', '')
                    if not title or not url:
                        continue
                    
                    # 获取发布时间
                    publish_time = yesterday
                    if 'publish_time' in item:
                        dt = datetime.fromtimestamp(item['publish_time'])
                        publish_time = dt.strftime('%Y-%m-%d')
                    
                    if publish_time != yesterday:
                        continue
                    
                    news_list.append(NewsItem(
                        title=title,
                        url=url,
                        publish_time=publish_time,
                        source="36氪",
                        summary=item.get('summary', '')[:200]
                    ))
                
                if news_list:
                    break
            except Exception as e:
                print(f"  [36氪] API解析失败: {e}")
                continue
        
        if not news_list:
            # 备用：网页爬取
            url = "https://36kr.com/information/technology/人工智能"
            html = self.fetch_page(url)
            
            if html:
                soup = BeautifulSoup(html, 'lxml')
                articles = soup.select('div.information-flow-item')[:10]
                
                for article in articles:
                    title_elem = article.select_one('a.title')
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text(strip=True)
                    url = title_elem.get('href', '')
                    
                    news_list.append(NewsItem(
                        title=title,
                        url=url,
                        publish_time=yesterday,
                        source="36氪",
                        summary=""
                    ))
        
        print(f"  [36氪] 获取到 {len(news_list)} 条新闻")
        return news_list


class TitaniumCrawler(BaseCrawler):
    """钛媒体 AI 新闻爬虫"""
    
    def __init__(self):
        super().__init__("钛媒体", "https://www.tmtpost.com")
    
    def crawl(self, days: int = 1) -> List[NewsItem]:
        """爬取钛媒体 AI 相关新闻"""
        news_list = []
        yesterday = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        # 尝试 RSS
        rss_urls = [
            "https://www.tmtpost.com/rss/人工智能",
            "https://www.tmtpost.com/rss/AI",
        ]
        
        for rss_url in rss_urls:
            html = self.fetch_page(rss_url)
            if not html:
                continue
            
            try:
                feed = feedparser.parse(html)
                
                for entry in feed.entries[:15]:
                    title = entry.get('title', '').strip()
                    url = entry.get('link', '')
                    if not title or not url:
                        continue
                    
                    publish_time = self._parse_time(entry.get('published', ''), yesterday)
                    
                    if publish_time != yesterday:
                        continue
                    
                    summary = entry.get('summary', '')
                    summary = re.sub(r'<[^>]+>', '', summary)
                    
                    news_list.append(NewsItem(
                        title=title,
                        url=url,
                        publish_time=publish_time,
                        source="钛媒体",
                        summary=summary[:200]
                    ))
                
                if news_list:
                    break
            except Exception as e:
                continue
        
        if not news_list:
            # 备用：网页爬取
            url = "https://www.tmtpost.com/tag/人工智能"
            html = self.fetch_page(url)
            
            if html:
                soup = BeautifulSoup(html, 'lxml')
                articles = soup.select('div.list-item')[:10]
                
                for article in articles:
                    title_elem = article.select_one('h2 a')
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text(strip=True)
                    url = title_elem.get('href', '')
                    
                    news_list.append(NewsItem(
                        title=title,
                        url=url,
                        publish_time=yesterday,
                        source="钛媒体",
                        summary=""
                    ))
        
        print(f"  [钛媒体] 获取到 {len(news_list)} 条新闻")
        return news_list
    
    def _parse_time(self, time_str: str, default: str) -> str:
        """解析时间字符串（支持多种格式）"""
        if not time_str:
            return default
        try:
            from email.utils import parsedate_to_datetime
            dt = parsedate_to_datetime(time_str)
            return dt.strftime('%Y-%m-%d')
        except:
            pass
        try:
            if 'T' in time_str:
                dt = datetime.fromisoformat(time_str.replace('Z', '+00:00').replace('+00:00', ''))
                return dt.strftime('%Y-%m-%d')
        except:
            pass
        try:
            dt = datetime.strptime(time_str[:10], '%Y-%m-%d')
            return dt.strftime('%Y-%m-%d')
        except:
            pass
        return default


class JiqizhixinCrawler(BaseCrawler):
    """机器之心 AI 新闻爬虫"""
    
    def __init__(self):
        super().__init__("机器之心", "https://www.jiqizhixin.com")
    
    def crawl(self, days: int = 1) -> List[NewsItem]:
        """爬取机器之心 AI 相关新闻"""
        news_list = []
        yesterday = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        # 尝试 API 方式
        api_url = "https://www.jiqizhixin.com/api/v1/articles"
        params = {'limit': 20, 'offset': 0}
        
        html = self.fetch_page(api_url)
        
        if html:
            try:
                data = json.loads(html)
                articles = data.get('data', {}).get('articles', [])
                
                for article in articles:
                    title = article.get('title', '').strip()
                    url = article.get('web_url', '')
                    if not title or not url:
                        continue
                    
                    publish_time = yesterday
                    if 'created_at' in article:
                        dt = datetime.fromisoformat(article['created_at'][:10])
                        publish_time = dt.strftime('%Y-%m-%d')
                    
                    if publish_time != yesterday:
                        continue
                    
                    news_list.append(NewsItem(
                        title=title,
                        url=url,
                        publish_time=publish_time,
                        source="机器之心",
                        summary=article.get('summary', '')[:200]
                    ))
                
                if news_list:
                    print(f"  [机器之心] 获取到 {len(news_list)} 条新闻")
                    return news_list
            except Exception as e:
                print(f"  [机器之心] API解析失败: {e}")
        
        # 备用：网页爬取
        urls = [
            "https://www.jiqizhixin.com/news",
            "https://www.jiqizhixin.com/research",
        ]
        
        for url in urls:
            html = self.fetch_page(url)
            if not html:
                continue
            
            soup = BeautifulSoup(html, 'lxml')
            articles = soup.select('div.news-item')[:10]
            
            for article in articles:
                title_elem = article.select_one('h3 a')
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True)
                url = title_elem.get('href', '')
                
                news_list.append(NewsItem(
                    title=title,
                    url=url,
                    publish_time=yesterday,
                    source="机器之心",
                    summary=""
                ))
            
            if news_list:
                break
        
        print(f"  [机器之心] 获取到 {len(news_list)} 条新闻")
        return news_list


class InfoQCrawler(BaseCrawler):
    """InfoQ AI 新闻爬虫"""
    
    def __init__(self):
        super().__init__("InfoQ", "https://www.infoq.cn")
        self.rss_url = "https://www.infoq.cn/topic/AI/recent"
    
    def crawl(self, days: int = 1) -> List[NewsItem]:
        """爬取 InfoQ AI 相关新闻"""
        news_list = []
        yesterday = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        # 尝试 RSS
        try:
            # InfoQ 的 RSS 源
            rss_urls = [
                "https://www.infoq.cn/rss",
                "https://www.infoq.cn/topic/AI",
            ]
            
            for rss_url in rss_urls:
                html = self.fetch_page(rss_url)
                if not html:
                    continue
                
                feed = feedparser.parse(html)
                
                for entry in feed.entries[:15]:
                    title = entry.get('title', '').strip()
                    url = entry.get('link', '')
                    if not title or not url:
                        continue
                    
                    # 检查是否包含AI相关内容
                    keywords = ['AI', '人工智能', '大模型', 'LLM', '机器学习', '深度学习']
                    if not any(k.lower() in title.lower() for k in keywords):
                        continue
                    
                    publish_time = self._parse_time(entry.get('published', ''), yesterday)
                    
                    if publish_time != yesterday:
                        continue
                    
                    summary = entry.get('summary', '')
                    summary = re.sub(r'<[^>]+>', '', summary)
                    
                    news_list.append(NewsItem(
                        title=title,
                        url=url,
                        publish_time=publish_time,
                        source="InfoQ",
                        summary=summary[:200]
                    ))
                
                if news_list:
                    break
        except Exception as e:
            print(f"  [InfoQ] RSS解析失败: {e}")
        
        if not news_list:
            # 备用：网页爬取
            url = "https://www.infoq.cn/topic/AI"
            html = self.fetch_page(url)
            
            if html:
                soup = BeautifulSoup(html, 'lxml')
                articles = soup.select('div.news-item')[:10]
                
                for article in articles:
                    title_elem = article.select_one('h3 a')
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text(strip=True)
                    url = title_elem.get('href', '')
                    
                    news_list.append(NewsItem(
                        title=title,
                        url=url,
                        publish_time=yesterday,
                        source="InfoQ",
                        summary=""
                    ))
        
        print(f"  [InfoQ] 获取到 {len(news_list)} 条新闻")
        return news_list
    
    def _parse_time(self, time_str: str, default: str) -> str:
        """解析时间字符串（支持多种格式）"""
        if not time_str:
            return default
        try:
            from email.utils import parsedate_to_datetime
            dt = parsedate_to_datetime(time_str)
            return dt.strftime('%Y-%m-%d')
        except:
            pass
        try:
            if 'T' in time_str:
                dt = datetime.fromisoformat(time_str.replace('Z', '+00:00').replace('+00:00', ''))
                return dt.strftime('%Y-%m-%d')
        except:
            pass
        try:
            dt = datetime.strptime(time_str[:10], '%Y-%m-%d')
            return dt.strftime('%Y-%m-%d')
        except:
            pass
        return default


class GitHubTrendingCrawler(BaseCrawler):
    """GitHub Trending AI 项目爬虫（备用数据源）"""
    
    def __init__(self):
        super().__init__("GitHub", "https://github.com")
    
    def crawl(self, days: int = 1) -> List[NewsItem]:
        """爬取 GitHub AI 相关热门项目"""
        news_list = []
        yesterday = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        # 尝试爬取 GitHub Trending AI 项目
        urls = [
            "https://github.com/trending/python?since=daily",
            "https://github.com/trending/ai?since=daily",
            "https://github.com/trending/machine-learning?since=daily",
        ]
        
        for url in urls:
            html = self.fetch_page(url)
            if not html:
                continue
            
            soup = BeautifulSoup(html, 'lxml')
            articles = soup.select('article.box-shadow')[:5]
            
            for article in articles:
                try:
                    title_elem = article.select_one('h2 a')
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text(strip=True)
                    title = re.sub(r'\s+', ' ', title)
                    
                    url = "https://github.com" + title_elem.get('href', '')
                    
                    # 获取描述
                    desc_elem = article.select_one('p')
                    summary = desc_elem.get_text(strip=True) if desc_elem else ""
                    
                    # 获取星标数
                    stars_elem = article.select_one('span.d-inline-block')
                    stars = stars_elem.get_text(strip=True) if stars_elem else ""
                    
                    if summary:
                        summary = f"{summary} {stars}".strip()
                    
                    news_list.append(NewsItem(
                        title=f"[GitHub Trending] {title}",
                        url=url,
                        publish_time=yesterday,
                        source="GitHub",
                        summary=summary[:200]
                    ))
                except Exception:
                    continue
            
            if news_list:
                break
        
        print(f"  [GitHub Trending] 获取到 {len(news_list)} 条项目")
        return news_list


class NewsGenerator:
    """新闻生成器"""
    
    def __init__(self, output_dir: str = "Daily"):
        self.output_dir = output_dir
        self.crawlers = [
            TechCrunchCrawler(),
            Kr36Crawler(),
            TitaniumCrawler(),
            JiqizhixinCrawler(),
            InfoQCrawler(),
            GitHubTrendingCrawler(),  # 备用数据源
        ]
    
    def crawl_all_news(self, days: int = 1) -> List[NewsItem]:
        """爬取所有来源的新闻"""
        all_news = []
        
        print("开始爬取 AI 资讯...")
        print("=" * 50)
        
        for crawler in self.crawlers:
            try:
                news = crawler.crawl(days)
                all_news.extend(news)
                time.sleep(1)  # 礼貌性延迟
            except Exception as e:
                print(f"  [{crawler.source_name}] 爬取出错: {e}")
                continue
        
        print("=" * 50)
        print(f"共获取 {len(all_news)} 条新闻")
        
        return all_news
    
    def deduplicate(self, news_list: List[NewsItem]) -> List[NewsItem]:
        """去重（基于标题哈希）"""
        seen = set()
        unique_news = []
        
        for news in news_list:
            # 标准化标题用于去重
            normalized_title = re.sub(r'[^\w\u4e00-\u9fff]', '', news.title.lower())
            title_hash = hashlib.md5(normalized_title.encode('utf-8')).hexdigest()
            
            if title_hash not in seen:
                seen.add(title_hash)
                unique_news.append(news)
        
        return unique_news
    
    def sort_by_source_priority(self, news_list: List[NewsItem]) -> List[NewsItem]:
        """按来源优先级排序"""
        priority = {
            "TechCrunch": 1,
            "36氪": 2,
            "钛媒体": 3,
            "机器之心": 4,
            "InfoQ": 5,
            "GitHub": 6,
        }
        
        return sorted(news_list, key=lambda x: (priority.get(x.source, 10), x.title))
    
    def generate_markdown(self, news_list: List[NewsItem], date_str: str = None) -> str:
        """生成 Markdown 格式内容"""
        if date_str is None:
            date_str = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
        
        # 去重并排序
        unique_news = self.deduplicate(news_list)
        sorted_news = self.sort_by_source_priority(unique_news)
        
        # 只取 Top10
        top_news = sorted_news[:10]
        
        # 生成 Markdown
        lines = [
            f"# {date_str} AI 热门资讯 Top10",
            "",
            f"收集时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
        ]
        
        for idx, news in enumerate(top_news):
            lines.append(f"## {idx}. [{news.title}]({news.url})")
            lines.append(f"- 来源：{news.source}")
            lines.append(f"- 发布时间：{news.publish_time}")
            if news.summary:
                lines.append(f"- 摘要：{news.summary}")
            lines.append("")
        
        return "\n".join(lines)
    
    def save_to_file(self, content: str, date_str: str = None) -> str:
        """保存到文件"""
        if date_str is None:
            date_str = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
        
        # 创建目录
        year_dir = os.path.join(self.output_dir, date_str[:4])
        os.makedirs(year_dir, exist_ok=True)
        
        # 生成文件名
        filename = f"{date_str}_AI热门资讯_Top10.md"
        filepath = os.path.join(year_dir, filename)
        
        # 写入文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filepath


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="AI News Crawler - AI资讯爬虫")
    parser.add_argument('--days', type=int, default=1, help='爬取几天前的新闻 (默认: 1)')
    parser.add_argument('--output', type=str, default='Daily', help='输出目录 (默认: Daily)')
    parser.add_argument('--test', action='store_true', help='测试模式：只爬取不保存')
    args = parser.parse_args()
    
    # 获取昨天日期
    yesterday = (datetime.now() - timedelta(days=args.days)).strftime('%Y%m%d')
    
    print(f"爬取日期: {yesterday}")
    print(f"输出目录: {args.output}")
    print()
    
    # 创建生成器
    generator = NewsGenerator(output_dir=args.output)
    
    # 爬取新闻
    all_news = generator.crawl_all_news(days=args.days)
    
    if not all_news:
        print("\n未获取到任何新闻，生成空文件...")
        content = f"""# {yesterday} AI 热门资讯 Top10

收集时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}

> 暂无新的AI资讯，可能是由于：
> - 网站反爬措施
> - 网络连接问题
> - 网站结构变化

## 建议
- 手动访问各资讯网站查看最新AI新闻
- 稍后重试运行爬虫
"""
    else:
        # 生成 Markdown
        content = generator.generate_markdown(all_news, date_str=yesterday)
    
    if args.test:
        # 测试模式：只打印内容
        print("\n" + "=" * 50)
        print("测试内容预览：")
        print("=" * 50)
        print(content)
    else:
        # 保存文件
        filepath = generator.save_to_file(content, date_str=yesterday)
        print(f"\n文件已保存: {filepath}")
        
        # 打印统计信息
        news_count = content.count("## ")
        print(f"共生成 {news_count} 条新闻条目")


if __name__ == "__main__":
    main()
