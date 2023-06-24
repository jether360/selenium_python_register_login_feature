from Access.access import Access

with Access() as bot:
    bot.land_first_page()

    #Register Affiliate
    #bot.join_now()
    #bot.input_affiliate_details()
    #bot.submit()

    #Log in Affiliate
    bot.login()
    bot.input_login_credentials()
    bot.submit()
