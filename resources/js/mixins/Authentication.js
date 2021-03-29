export const authentication = {

    methods: {

        do_hosted_auth(emailHint, scopeType, scopes ) {
            let nylas_auth_url = 'https://api.nylas.com/oauth/authorize';

            let app = this;
            this.createCookie('connect_' + scopeType)

            const myUrl = new URL(nylas_auth_url);
            myUrl.searchParams.append("login_hint", emailHint);
            myUrl.searchParams.append("client_id", nylas_app_client_id);
            myUrl.searchParams.append("response_type", "token");
            myUrl.searchParams.append("redirect_uri", nylas_call_back_url);
            myUrl.searchParams.append("scopes", scopes);
            myUrl.searchParams.append("state", "CSRF_TOKEN");

            console.log(myUrl);

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
