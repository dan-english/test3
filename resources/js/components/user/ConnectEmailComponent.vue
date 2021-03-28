<template>
<div class="wrapper_container" v-if="loaded">

       <div class="row row_header">
                <div class="col-sm-12">
                  Email Sync
                  <div class="row_header_button row_header_button_advanced hidden-xs-only">Advanced</div>
                </div>
          </div>

       <div class="row row_box">
            <div class="col-md-12">
                  <div class="row_header_description row_header_description_full">
                       <h3>Unlock your Sales Inbox</h3>
                      <div>Tab switching and manually forwarding emails is a thing of the past. <br>When unlocked, you can use your Sales Inbox to send emails directly while automatically linking them to related deals and contacts.</div>

                   <ul class="ticklist">
              <li><i class="green_tick el-icon-check"></i>Sync emails with any major email provider</li>
              <li><i class="green_tick el-icon-check"></i>Track email opens and clicks</li>
              <li><i class="green_tick el-icon-check"></i>Save time by making use of customizable templates</li>
              <li><i class="green_tick el-icon-check"></i>Customize your signature for a more professional look</li>
            </ul>
                  </div>
            </div>
        </div>

        <connected-accounts-component
          :user_email="useremail"
          :scopedata="scope_data">
        </connected-accounts-component>

        <div class="row row_box" id="smart_bcc_addresses">
            <div class="col-md-12">
                  <div class="row_header_description row_header_description_full">
                       <h3>Smart email BCC address</h3>
                      <div>Add your Smart BCC address to the Cc or Bcc line when emailing customers or forward incoming emails to this address to automatically copy your emails.
                          Once authorized, you'll be able to copy any email you wish using the Smart BCC feature.<br>
                          The email address has to be unique, so make sure the address is not already being used by another account.
                        </div>
                    <div> <el-input v-model="bccemail" type="email" placeholder="Add an alternative email" style="width:500px"></el-input>
                <el-button type="primary" plain @click="add_bcc_email_address()">Add</el-button></div>

              <el-tag
                  v-for="tag in bccemails"
                  :key="tag.name"
                  @close="handleClose(tag)"
                  closable
                  style="font-size:10px;margin-top:10px; margin-right:5px;"
                  :type="tag.type">
                  {{tag.name}}
                </el-tag>
                  </div>
            </div>
        </div>
        <div class="row row_box" id="default_email_sharing">
                  <div class="col-sm-12">
                          <div class="row_header_description row_header_description_full">
                                  <h3>Default email sharing</h3>
                                  <table>
                                        <tr>
                                          <td>
                                            <el-radio v-model="shareradio" label="1" size="mini"> </el-radio>
                                          </td>

                                          <td style="padding-left:10px;font-size:10px"  @click="shareradio='1'">
                                              <div style="font-weight:bold">Share all my linked email conversations with others in my company</div> Email conversations will be visible to others only when they are linked to contacts and deals.
                                          </td>
                                        </tr>

                                        <tr>
                                          <td>
                                            <el-radio v-model="shareradio" label="2"></el-radio>
                                          </td>
                                          <td style="padding-left:10px;;font-size:10px" @click="shareradio='2'">
                                              <div style="font-weight:bold;">Keep all my email conversations private</div> Email conversations can still be linked to contacts and deals, but they will only be visible to you.
                                          </td>
                                        </tr>
                                  </table>
                          </div>
                  </div>
        </div>
        <div class="row row_box" id="lead_linking">
                <div class="col-sm-12">
                      <div class="row_header_description row_header_description_full">
                            <h3>Link emails to leads and deals</h3>
                                <table>
                                  <tr>
                                      <td>
                                        <el-radio v-model="linkradio" label="1" > </el-radio>
                                      </td>
                                      <td style="padding-left:10px;font-size:10px"  @click="linkradio='1'">
                                          <div style="font-weight:bold;margin-bottom:10px;">Link emails manually</div>
                                      </td>
                                  </tr>


                                  <tr>
                                    <td>
                                        <el-radio v-model="linkradio" label="2"></el-radio>
                                    </td>
                                    <td style="padding-left:10px;;font-size:10px" @click="linkradio='2'">  <div style="font-weight:bold;">Automatically link emails to leads or deals</div>Look for an open lead or deal related to the contact person the email was sent to or received from. When only one open lead or deal is found that matches the contact person, the email will be linked to it automatically.</td>
                                  </tr>
                                </table>
                      </div>
                </div>
        </div>



</div>


</template>

<style></style>
<script>

    export default {
        name:'ConnectEmail',
        props:['email','token','refresh'],
        data() {
            return {
              loaded: false,
              useremail:'',
              accesstoken:'',
              bccemail:'',
              shareradio:'1',
              linkradio:'1',
              bccemails: [
                 { name: 'someone@somewhere.com', type: 'success' },
              ],
              newAccountEmail:'',
              scope_data: {
                    'type':'email',
                   'scopes':'email.modify,email.send',
              },
              renderComponent:true

            }


        },
        watch:{},
        mounted() {
          this.useremail = this.email
          this.accesstoken = this.token
          this.loaded =true
        },

        methods: {
          handleClose(tag) {
                this.bccemails.splice(this.bccemails.indexOf(tag), 1);
          },
          handleSelectionChange(row,index) {

          },
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



        },


    }
</script>
