<template>

<div class="wrapper_container" v-if="loaded">

          <div class="row row_header">
                <div class="col-sm-12">
                  Demo Settings
                  <div class="row_header_button row_header_button_advanced hidden-xs-only">Advanced</div>
                </div>
          </div>

        <div class="row row_box ">
            <div class="col-md-12">
                  <div class="row_header_description">
                       <h3>Configure settings for your demo account here</h3>
                      <div>These settings will persist betwen browsers/logins so you can ensure consistency for your demos.
                      These settings will be specific to your current user and are not shared with other users.</div>
                  </div>
                 <img class="desc_image" width="100px" src="/images/nylas_black.png">
            </div>
        </div>

        <div class="row row_box">
            <div class="col-sm-12">
                      <el-input style="width:200px;padding-top:15px;" v-model="connect_accounts_email_address" placeholder="Name" size="mini"></el-input>
                      <el-button @click="createConnectedAccounts()" type="primary" plain size="mini">Go</el-button>
                      <div style="margin-top:15px;font-size:11px;"><i class="el-icon-info"></i> We will add the domains, just give us a name eg (dan.english)</div>
            </div>
        </div>

   <el-dialog
      title="No Name Provided"
      :visible.sync="demoAccountCreationWarning"
      width="30%">
      <span>Please enter a name to create accounts for</span>
      <span slot="footer" class="dialog-footer"><el-button type="primary" @click="demoAccountCreationWarning = false">Okay</el-button>
      </span>
   </el-dialog>

</div>

</template>
<style></style>

<script>
    export default {
        name:'ProfileComponent',
        props: ['userdata'],
        data() {
            return {
              loaded:false,
              activeTab: 'first',
              user:{},
              connect_accounts_email_address:'',
              demoAccountCreationWarning:false,
            }
        },
        mounted() {
            this.user = this.userdata;
            // this.connect_accounts_email_address = this.user.email
            this.loaded = true;
        },

        methods: {


          createConnectedAccounts() {
            if(!this.connect_accounts_email_address) {
              console.error('No Email Address')
              this.demoAccountCreationWarning=true
              return 0;
            }
            console.log('create demo accounts for:' + this.connect_accounts_email_address)
            axios.post('/demo-data/accounts',{'name':  this.connect_accounts_email_address}).then((response)=>{
              console.log(response.data)
            })

          }

        }
    }

</script>

