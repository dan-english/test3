export const authentication = {

    methods: {

        do_hosted_auth(emailHint, scopeType, scopes ) {

            let nylas_auth_url = process.env.VUE_APP_NYLAS_OAUTH_ENDPOINT
            let nylas_app_client_id = process.env.VUE_APP_NYLAS_APP_CLIENT_ID
            let call_back_url = process.env.VUE_APP_CALL_BACK_URL

            let app = this;
            this.createCookie('connect_' + scopeType)

            const myUrl = new URL(nylas_auth_url);
            myUrl.searchParams.append("login_hint", emailHint);
            myUrl.searchParams.append("client_id", nylas_app_client_id);
            myUrl.searchParams.append("response_type", "token");
            myUrl.searchParams.append("redirect_uri", call_back_url);
            myUrl.searchParams.append("scopes", scopes);
            myUrl.searchParams.append("state", "CSRF_TOKEN");

            var win = window.open(myUrl, "MsgWindow", "width=600,height=800");

            var checkConnect;
            checkConnect = setInterval(function() {
                   if (!win || !win.closed) return;
                   clearInterval(checkConnect);
                   app.getAccountData();
               }, 100);

        },
      createCookie(type){
              if(type) {
                  var date = new Date();
                  date.setTime(date.getTime() + (1*24*60*60*1000));
                  document.cookie = "callbackpage="+type+";path=/; expires=" + date.toUTCString();
              }
          },
    }
};
