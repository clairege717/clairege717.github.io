# 20200602 jekyll new . --force 出错

错误详情：
```
 ~/Documents/workspace/GitHub/clairege717.github.io >> jekyll serve -H 192.168.51.102 -w
    Traceback (most recent call last):
        15: from /usr/local/bin/jekyll:23:in `<main>'
        14: from /usr/local/bin/jekyll:23:in `load'
        13: from /Library/Ruby/Gems/2.6.0/gems/jekyll-4.0.0/exe/jekyll:11:in `<top (required)>'
        12: from /Library/Ruby/Gems/2.6.0/gems/jekyll-4.0.0/lib/jekyll/plugin_manager.rb:52:in `require_from_bundler'
        11: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.4/lib/bundler.rb:149:in `setup'
        10: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.4/lib/bundler/runtime.rb:20:in `setup'
         9: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.4/lib/bundler/runtime.rb:101:in `block in definition_method'
         8: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.4/lib/bundler/definition.rb:226:in `requested_specs'
         7: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.4/lib/bundler/definition.rb:237:in `specs_for'
         6: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.4/lib/bundler/definition.rb:170:in `specs'
         5: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.4/lib/bundler/definition.rb:258:in `resolve'
         4: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.4/lib/bundler/resolver.rb:22:in `resolve'
         3: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.4/lib/bundler/resolver.rb:49:in `start'
         2: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.4/lib/bundler/resolver.rb:258:in `verify_gemfile_dependencies_are_found!'
         1: from /Library/Ruby/Gems/2.6.0/gems/bundler-2.1.4/lib/bundler/resolver.rb:258:in `each'
/Library/Ruby/Gems/2.6.0/gems/bundler-2.1.4/lib/bundler/resolver.rb:290:in `block in verify_gemfile_dependencies_are_found!': Could not find gem 'tzinfo-data' in any of the gem sources listed in your Gemfile. (Bundler::GemNotFound)
```

解决方案：
```
~/Documents/workspace/GitHub/clairege717.github.io >> bundle exec jekyll serve
    Could not find gem 'tzinfo-data' in any of the gem sources listed in your Gemfile.
    Run `bundle install` to install missing gems.
~/Documents/workspace/GitHub/clairege717.github.io >> bundle install     
    ...   
```