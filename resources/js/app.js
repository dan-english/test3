import styles from '../../resources/scss/styles.scss'

// PACKAGES BEING INSTALLED VIA CDN TO KEEP THE APP.JS AS SMALL AS POSSIBLE


let token = document.head.querySelector('meta[name="csrf-token"]');

if (token) {
    window.axios.defaults.headers.common['X-CSRF-TOKEN'] = token.content;
}


Vue.component('profile-component', require('/resources/js/components/user/ProfileComponent').default);
Vue.component('connect-calendar-component', require('/resources/js/components/user/ConnectCalendarComponent').default);
Vue.component('connect-email-component', require('/resources/js/components/user/ConnectEmailComponent').default);
Vue.component('connect-contacts-component', require('/resources/js/components/user/ConnectContactsComponent').default);
Vue.component('personal-details-component', require('/resources/js/components/user/PersonalDetailsComponent').default);
Vue.component('connected-accounts-component', require('/resources/js/components/user/ConnectedAccountsComponent').default);
Vue.component('crm-demo-settings-component', require('/resources/js/components/user/CRMDemoSettingsComponent').default);

Vue.component('timezone-component', require('/resources/js/components/TimezoneComponent').default);
Vue.component('open-hours-component', require('/resources/js/components/user/OpenhoursComponents').default);
Vue.component('interface-options-component', require('/resources/js/components/user/InterfaceOptionsComponent').default);


Vue.component('inbox-component', require('/resources/js/components/email/InboxComponent').default);
Vue.component('message-component', require('/resources/js/components/email/MessageComponent').default);
Vue.component('sidebar-component', require('/resources/js/components/email/SidebarComponent').default);
Vue.component('email-demo-panel-component', require('/resources/js/components/email/EmailDemoPanelComponent').default);


Vue.component('deals-leads-component', require('/resources/js/components/deals/DealsLeadsComponent').default);
Vue.component('deal-summary-component', require('/resources/js/components/deals/DealSummaryComponent').default);
Vue.component('console-drawer-component', require('/resources/js/components/console/ConsoleDrawerComponent').default);
Vue.component('console-table-component', require('/resources/js/components/console/ConsoleTableComponent').default);

Vue.component('contacts-component', require('/resources/js/components/contacts/ContactsComponent').default);


Vue.config.productionTip = false;
Vue.config.debug = false;
Vue.config.silent = true;
Vue.config.devtools = false;

const app = new Vue({
    el: '#app',
    data: {
        pusher_messages: [],
      },

});
