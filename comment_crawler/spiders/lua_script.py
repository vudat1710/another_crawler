click_script = """
    function main(splash)
        local num_clicks = splash.args.num_clicks
        local click_delay = splash.args.click_delay
        local crawl_comment = splash.args.is_crawling_comment

        local click_button
        if crawl_comment == "comment" then
            click_button = splash:jsfunc([[
                function () {
                    document.querySelector("div[class='pn-loadmore fd-clearbox ng-scope'] > a").click();
                }
            ]])
        else
            click_button = splash:jsfunc([[
                function () {
                    document.querySelector("div[class='btn-load-more ng-scope ng-enter-prepare'] > a").click();
                }
            ]])
        end
        assert(splash:go(splash.args.url))
        splash:wait(splash.args.wait)

        for _ = 1, num_clicks do
            click_button()
            splash:wait(click_delay)
        end
        return splash:html()
    end
"""


scroll_script = """
    function main(splash)
        local num_scrolls = splash.args.num_scrolls
        local scroll_delay = splash.args.scroll_delay
        local scroll_func = splash:jsfunc("window.scrollTo")
        local get_scroll_height = splash:jsfunc([[
            function() {
                return document.body.scrollHeight;
            }
        ]])
        assert(splash:go(splash.args.url))
        splash:wait(splash.args.wait)

        for _ = 1, num_scrolls do
            local scroll_height = get_scroll_height()
            for i = 1,10 do
                scroll_func(0, scroll_height * i / 10)
                splash:wait(scroll_delay / 10)
            end
        end
        return splash:html()
    end
"""