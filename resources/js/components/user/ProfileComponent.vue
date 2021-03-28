<template>
    <div class="container" v-if="loaded">
         <el-tabs v-model="activeTab" @tab-click="handleTabClick">
              <el-tab-pane label="Personal Details" name="first">
                      <personal-details-component :user_details="user"></personal-details-component>
              </el-tab-pane>
              <el-tab-pane label="Email Sync" name="second">
                <connect-email-component :email="user.email" :token="user.access_token"></connect-email-component>
              </el-tab-pane>
              <el-tab-pane label="Calendar Sync" name="third">
                <connect-calendar-component
                      :email="user.email"
                      :token="user.access_token">
                </connect-calendar-component>


              </el-tab-pane>
              <el-tab-pane label="Contact Sync" name="fourth">
              <connect-contacts-component
                 :email="user.email"
                :token="user.access_token">

              </connect-contacts-component>

              </el-tab-pane>

        <el-tab-pane label="Demo Settings" name="fifth">
          <crm-demo-settings-component :user_details="user"></crm-demo-settings-component>
        </el-tab-pane>
         </el-tabs>
    </div>
</template>


<script>
    export default {
        name:'ProfileComponent',
        props: ['userdata',],
        data() {
            return {
              loaded:false,
              activeTab: 'first',
              user:{},
            }
        },
        mounted() {
            this.user = this.userdata;
            this.loaded = true;
        },

        methods: {
             handleTabClick(tab) {},
        }
    }

</script>

