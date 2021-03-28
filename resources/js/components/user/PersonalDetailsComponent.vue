<template>
<div class="wrapper_container" v-if="loaded">
          <div class="row row_header">
                <div class="col-sm-12">
                  Personal Details



                </div>
          </div>

          <div class="row row_box ">
              <div class="col-md-12">
                    <div class="row_header_description">
                         <h3>Update your personal details</h3>
                        <div>Here you can personalise your experience on the platform by authenticating and configuring things like your timezone</div>
                    </div>
                <el-upload
  class="avatar-uploader desc_image"
  action="/avatar"
  :show-file-list="false"
  :on-success="handleAvatarSuccess"
  :before-upload="beforeAvatarUpload">
  <img v-if="getProfileImage()" :src="getProfileImage()" class="avatar">
  <i v-else class="el-icon-plus avatar-uploader-icon"></i>
</el-upload>

              </div>
          </div>


             <div class="row row_box" >

                <div class="col-md-12">
                                <div style="font-weight:Bold;font-size:14px;text-align:left;padding-bottom:15px;padding-top:15px">General Details</div>

    <table id="personaldetails_table">
            <tr><td>Your name</td><td><el-input v-model="user.name"></el-input></td></tr>
            <tr><td>Email</td><td><el-input disabled v-model="user.email"></el-input></td></tr>
            <tr><td>Phone</td><td><el-input v-model="user.mobile_number"></el-input></td></tr>

            <tr><td>Timezone</td><td><timezone-component
                                      :currenttimezone="user.time_zone"
                                      v-on:timezonechanged="updateTimeZone"></timezone-component></td></tr>

            <tr>
              <td>Date/number format</td>
              <td>
                <el-select v-model="numberformat">

                <el-option
                  v-for="(item, index) in numberformats"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>

                </el-select>
            </td>

            </tr>



            <tr><td>Language</td><td>
              <el-select v-model="user.language">
                 <el-option
      v-for="(item, index) in languages"
      :key="item.value"
      :label="item.label"
      :value="item.value"
      >
    </el-option>
              </el-select>
            </td></tr>
            <tr><td>Currency</td><td><el-select v-model="user.currency">
               <el-option
      v-for="(item, index) in currencies"
      :key="item.value"
      :label="item.label"
      :value="item.value"
      >
    </el-option>
              </el-select></td></tr>


            <!-- master demo auth token -->
            <tr>
              <td>Access Token</td>
              <td>

                <el-input disabled v-model="user.access_token" v-bind:class="isValid">
                      <template slot="append"><el-button @click="authMasterToken()"><i class="el-icon-link"></i></el-button></template>
                </el-input>
                <sub v-if="!isValid">Your token is currently invalid, reauthenticate to get a new token</sub>
                <sub><i class="el-icon-question"></i>This token has all available scopes and you can use this token in postman </sub>

              </td>
            </tr>

          </table>


         <div class="row" style="float:right">
              <div class="col-md-12"><el-button @click="updateUserDetails()">Save Details</el-button></div>
         </div>

                  </div>
               </div>
      <open-hours-component :userdata="user"></open-hours-component>
      <interface-options-component></interface-options-component>



</div>
</template>

<style>
#personaldetails_table tr>td {
  padding-bottom: 10px;
}

#personaldetails_table input {
  height:25px;
  border-radius:0;
  line-height:25px;
}
.el-input__icon {
    line-height:25px;
}



.calendar_sync_container {
  background-color:white;
  padding-top:10px;
  border:1px solid #ccc;
}

.calendar_sync_header {
  border-bottom:1px solid #ccc;
}
.calendar_sync_header h1{
  font-size:25px;
}


table td {
  text-align:left;
}



.interfacelist{
  text-align:left;
list-style:none;
}




  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 50px;
    height: 50px;
    line-height: 50px;
    text-align: center;
  }
  .avatar {
    width: 50px;
    height: 50px;
    display: block;
  }

</style>
<script>
    import {authentication} from '../../mixins/Authentication'

    export default {
        name:'PersonalDetails',
        props:['user_details'],
        mixins: [authentication],

        data() {
            return {
              loaded: false,
              user:{},
              imageUrl: '',


              currency:'US Dollar (USD)',
              currencies:[
                        {
                          label: 'US Dollar (USD)',
                          value:'usd'},
                        {
                          label:'Pound Sterling (GBP)',
                          value:'gbp',
                        },
                        {
                          label:'Euro (EUR)',
                          value:'eur'
                        }
                 ],

              language:'English (US)',
              languages:[
                  {
                          label: 'English (US)',
                          value:'eng_us'},
                        {
                          label:'English (UK)',
                          value:'eng_uk',
                        },
                        {
                          label:'Japanese',
                          value:'japanese',
                        },{
                          label:'French',
                          value:'french',
                        },
              ],

              numberformat:'English (United States)',
              numberformats:[
                  {
                          label: 'English (United States)',
                          value:'num_us'
                  },
                  {
                          label: 'English (United Kingdom)',
                          value:'num_uk'
                  },
              ],

            }

        },

        mounted() {
          this.user = this.user_details;
          if (this.user.avatar) {
            this.imageUrl = '/static/' + this.user.avatar;
          }
          this.loaded = true
        },

        computed: {
            isValid () {
                if(this.user.validToken) {
                  return 'valid-token'
                }

                return 'invalid-token'
            }
        },

        methods: {
          getProfileImage() {
             if (this.user.avatar.trim()) {
               return '/uploads/' +this.user.avatar
             }
             return undefined
          },
          handleClose(tag) {
                this.bccemails.splice(this.bccemails.indexOf(tag), 1);
          },
          handleSelectionChange(row,index) { },
          checkAuthentication() {
            return 'error'
          },

          add_bcc_email_address() {
                 console.log(this.bccemail);
                 this.bccemails.push({
                   'name':this.bccemail,
                   'type':'success'
                 })

          },
          updateTimeZone(value) {
            this.user.time_zone = value
          },

          handleAvatarSuccess(res, file) {
            this.imageUrl = URL.createObjectURL(file.raw);
            this.user.avatar = file.response;
            this.updateUserDetails();

          },

          beforeAvatarUpload(file) {
              const isJPG = file.type === 'image/jpeg';
              const isLt2M = file.size / 1024 / 1024 < 2;

              if (!isJPG) {
                this.$message.error('Avatar picture must be JPG format!');
              }
              if (!isLt2M) {
                this.$message.error('Avatar picture size can not exceed 2MB!');
              }

              return isJPG && isLt2M;
      },

          getUserDetails() {
             axios.get('/profile/details').then((response)=>{
                  this.user= response.data
             });
          },
          updateUserDetails() {
            let data = this.user;
            axios.post('/profile/update', {'user_data':data})
                .then((response => {
                  console.log(response.data)
                })
            )
          },

          authMasterToken() {
            //call the mixin function
               this.do_hosted_auth(this.user.email, 'personal', '' )
          },

          getAccountData () {
                let app = this;
                axios.get('/profile/details').then((response) => {
                       app.$set(app.user, 'access_token', response.data.access_token )
                });
          },


        },


    }
</script>
