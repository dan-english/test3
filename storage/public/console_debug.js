if (typeof app_debug === 'undefined') {
    console.error ('**** app_debug Flag Not Found - Please Update Your Environment File ****');
    var app_debug = 1; //nasty
}
//something here
var _debug = {

    group: function (message) {
        (app_debug === 1) ? console.groupCollapsed('%c'+message, 'color:#228B22;font-size: normal;font-weight:bold;') : undefined;
    },

    groupEnd: function () {
        (app_debug === 1) ? console.groupEnd() : undefined;
    },

    groupMessage: function(name, message) {
        _debug.group(name);

        if(typeof(message) == 'object') {
            console.table(_.zipObject(Object.keys(message), Object.values(message)));
        }
        else {
            _debug.info(message);
        }

        _debug.groupEnd();
    },

    mounted: function(message) {
        if(app_debug === 1) {
            if(typeof(message) == 'string') {
                console.info('%c'+ '[mounted] ' +message, 'color: red; font-size: normal;font-weight:bold;font-style:italic');
            }
            else {
                console.info(message);
            }
        }
    },

    info: function(message) {
        if(app_debug === 1) {
            if(typeof(message) == 'string') {
                console.info('%c'+ '[i] ' +message, 'color: blue; font-size: normal;font-weight:bold;font-style:italic');
            }
            else {
                console.info(message);
            }
        }
    },

    infoWarn: function(message) {
        if(app_debug === 1) {
            if(typeof(message) == 'string') {
                console.info('%c'+ '[w] ' +message, 'color: #999900; font-size: normal;font-weight:bold;font-style:italic');
            }
            else {
                console.info(message);
            }
        }
    },

    infoError: function(message) {
        if(app_debug === 1) {
            if(typeof(message) == 'string') {
                console.info('%c'+ '[e] ' +message, 'color: red; font-size: normal;font-weight:bold;font-style:italic');
            }
            else {
                console.info(message);
            }
        }
    },

    msg: function(message) {
        (app_debug === 1) ? console.debug('%c'+message, 'color: green; font-size: normal;font-weight:bold;') : undefined;
    },

    log: function(message) {
        if(app_debug === 1) {
            if(typeof(message) == 'string') {
                console.log('%c'+message, 'color: #384D69; font-size: normal;font-weight:normal;');
            }
            else {
                console.log(message);
            }
        }
    },

    warn: function(message) {
        (app_debug === 1) ? console.warn('%c'+message, 'color: #84D69; font-size: normal;font-weight:bold;') : undefined;
    },
    error: function(message) {
        (app_debug === 1) ? console.error('%c'+message, 'color: #384D69; font-size: normal;font-weight:bold;') : undefined;
    },
    table: function(dataArray) {
        (app_debug === 1) ? console.table(dataArray) : undefined;
    },

    image: function(t) {
        if(app_debug === 1) {
            console.log('%c    ', 'font-size:300px; background-size: 100% 100%; background:url('+t+') no-repeat;');
        }
    },

    authInfo: function(urlObject) {
        // let searchParams = new URLSearchParams(urlObject.search);
        // let requestObject = {
        //     // origin: urlObject['origin'],
        //     // protocol: urlObject['protocol'],
        //     // host: urlObject['host'],
        //     // pathname: urlObject['pathname'],
        //     href :urlObject['href'],
        // };
        // searchParams.forEach(function(value, key) {
        //     switch(key) {
        //
        //         case 'scopes':
        //             updatedKey=key + ' (the permissions needed for your app)'
        //             break;
        //         case 'login_hint':
        //             updatedKey=key + ' (the users email address)'
        //             break;
        //         case 'client_id':
        //             updatedKey=key + ' (of the Nylas App)'
        //             break;
        //
        //         default:
        //             updatedKey=key
        //     }
        //     requestObject[updatedKey] = value;
        // });
        // console.info('%c'+ '[AUTH_URL] ' +urlObject['href'], 'color: green; font-size: 15px;font-weight:bold;font-style:italic');
        //
        // console.table(requestObject);
    },


    config(data) {
        data.app_debug_enabled = app_debug;

        console.groupCollapsed('%cConfiguration', 'color:#384D69;font-size: normal;font-weight:bold;');
        console.table(data);

        console.groupEnd();


    },

    apiRequest(data) {
        var css = 'background-color:#00E5BF;display:block;border:1px solid #696969;border-radius:5px;padding:2px;'
        console.groupCollapsed('%cNYLAS API REQUEST ['+data.endpoint+']', css);
        console.log(data);
        console.groupEnd();
    },
    apiResponse(data) {
        var css = 'background-color:#ccf;display:block;border:1px solid #696969;border-radius:5px;padding:2px;'
        console.groupCollapsed('%cNYLAS API REQUEST ['+data.endpoint+']', css);
        console.log(data);
        console.groupEnd();
    }

};
