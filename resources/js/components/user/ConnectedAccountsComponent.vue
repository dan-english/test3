<template>
<div class="" v-if="loaded">

   <!-- connected accounts -->
    <div class="row row_box" id="smart_bcc_addresses" style="border:none;margin:0px;padding:0px;" >


            <div class="col-md-12">
              <div class="row_header_description row_header_description_full">

                <h3 style="width:150px;float:left;">Connected accounts</h3>

                  <div class="refresh_icon" @click="refresh()" title="Refresh Accounts">
                          <i class="el-icon-refresh"></i>
                  </div>

              </div>


              <div>

                <el-input style="width:200px;padding-top:15px;padding-bottom:10px;" v-model="newAccountEmail" placeholder="user@provider.com" size="mini"></el-input>
<el-button @click="addNewAccount(newAccountEmail)" type="primary" plain size="mini">Add new account</el-button>
                      <div v-if="newAccountError" class="newaccounterror">Please enter an email address</div>

              </div>




            </div>
    </div>

    <div class="row row_box connected_account" v-for="connectedAccount in connectedAccounts">

          <div class="col-md-1 " style="text-align:left;margin-top:20px;">
              <i class="account-icon">
                <img style="width:25px;" :src="getProviderImage(connectedAccount.provider)">
              </i>
          </div>

          <div class="col-md-8 col-sm-5" style="text-align:left;margin-top:15px;">
                <div class="email" >{{ connectedAccount.email }}</div>
                <div v-if="!connectedAccount.valid" class="auth_error"><i class="el-icon-warning"></i>&nbsp;Authentication Error</div>
                <div v-if="connectedAccount.valid" ><i class="green_tick el-icon-check"></i>Account is syncing</div>
          </div>

          <div class="col-md-3 col-sm-1" style="margin-top:15px;">
            <div class="row"><div class="col-sm-12">
<el-button style="width:140px" @click="connectAccount(connectedAccount.email)" plain type="warning"  size="small" v-if="!connectedAccount.valid">Re-Authenticate</el-button>
              </div></div>
            <div class="row"><div class="col-sm-12">
<el-button style="width:140px" @click="connectAccount(connectedAccount.email)" plain type="success" size="small" v-if="connectedAccount.valid">Generate New Token</el-button>
              </div></div>
            <div class="row" style="padding-top:5px;">
               <div class="col-sm-12">
<el-button style="width:140px" @click="deleteConnectedAccount(connectedAccount)" plain type="danger" size="small" >Delete Account</el-button>
                 </div>
</div>


          </div>

    </div>


      <!-- connected accounts -->




    </div>
</template>
<style>
.refresh_icon {
color: #409EFF;
    background: #ecf5ff;
    border-color: #b3d8ff;
  width:25px;
  height:25px;
  border:1px solid;
  line-height:25px;
  text-align:center;
  font-weight:bold;
  border-radius:3px;
  float:right;
}

.refresh_icon:hover {
      background: #409eff;
  color:white;
cursor:pointer;
}






.delete_account{
height:10px;
  width:2px!important;
  line-height:10px;
  margin:0px;
  padding:0px;


}

.close_icon{
  font-size:10px;

  font-weight:bold;

  height:20px;
  line-height:1px;


}





.auth_error {
  color:#F56C6C;
  font-weight:bold;
}
.new_account {
  text-align:left;
  border:1px solid #ccc;
}
.new_account input {
  border-radius:0;
  width:250px;
}

.newaccounterror {
  text-transform: uppercase;
  color:red;
  font-size:10px;

  padding-left:10px;
}

</style>
<script>
import {authentication} from '../../mixins/Authentication'

    export default {
      mixins: [authentication],
      props:['scopedata','user_email'],
       data() {
         return {
           loaded: false,
           connectedAccounts:[],
           newAccountEmail:'',
           newAccountError:0,
           scope_data:{},
           useremail:'',
         }
       },
       mounted() {
           this.scope_data = this.scopedata;
           this.useremail = this.user_email;

           this.getAccountData();
       },
       methods: {
        refresh() {
          this.getAccountData()
        },
         addNewAccount() {
           this.newAccountError=0;
           if(this.newAccountEmail === undefined || this.newAccountEmail === null || this.newAccountEmail === '') {
             this.newAccountError=1
           }
           else{
           this.connectAccount(this.newAccountEmail)
             }
         },

         getAccountData() {
              let url = '/accounts/email'

               if (this.scope_data.type === 'calendar') {
                 url = '/accounts/calendar';
               }
               else if(this.scope_data.type === 'contact') {
                 url = '/accounts/contact';
               }
               axios.get(url).then((response)=>{
                    // this.$set(this.connectedAccounts, response.data)
                    this.connectedAccounts = response.data
                }).then(()=>{
                if (this.connectedAccounts.length == 0) {
                    this.newAccountEmail = this.useremail
                }
                this.loaded=true
               })



          },
         getProviderImage(provider){

           if(provider === 'google') {
                return '/images/googleicon.svg';
           }
           if(provider === 'gmail') {
                return '/images/googleicon.svg';
           }
           if(provider === 'outlook') {
               return '/images/outlook.png';
           }
        if(provider === 'apple') {
               return '/images/apple-logo.png';
           }
           if(provider === 'yahoo') {
               return '/images/yahoo.png';
           }
           if(provider === 'office365') {
               return '/images/office365.png';

           }

         },

          connectAccount(emailHint) {
              this.do_hosted_auth(emailHint, this.scope_data.type, this.scope_data.scopes )
          },

          deleteConnectedAccount(account){

            axios.post('/accounts/delete', {'data':account}).then((response)=>{
              if(response.data == 1) {
                let i = this.connectedAccounts.map(item => item.id).indexOf(account.id);
                this.connectedAccounts.splice(i, 1);
              }
            })


          },
       }

    }
</script>
