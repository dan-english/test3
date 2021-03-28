<template>
<div class="wrapper_container" v-if="loaded">

    <div class="row row_header">
                <div class="col-sm-12">
                  Calendar Sync
                  <div class="row_header_button row_header_button_easy hidden-xs-only">Easy</div>
                </div>
    </div>

          <div class="row row_box ">
            <div class="col-md-12">
                  <div class="row_header_description">
                       <h3>See all your activities in one place</h3>
                      <div>
                            <ul class="callist">
                                   <li>Stop switching between Platforms and your external calendar</li>
                                   <li>Share your availability and propose meeting times with Scheduler</li>
                                    <li>Never miss an activity or make a double-booking again</li>
                            </ul>
                      </div>
                    <div>Sync your events with major calendar providers including:</div>
              <table>
                  <tr>
                    <td><i class="green_tick el-icon-check"></i>Google</td>
                    <td><i class="green_tick el-icon-check"></i>Apple</td>
                  </tr>
                  <tr>
                    <td><i class="green_tick el-icon-check"></i>Microsoft Exchange</td>
                    <td><i class="green_tick el-icon-check"></i>Microsoft Office 365</td>
                  </tr>
                <tr>
                    <td><i class="green_tick el-icon-check"></i>Outlook.com</td>
                  </tr>
             </table>
                  </div>
                 <img class="desc_image" width="100px" src="/images/cal.svg">
            </div>
        </div>


    <connected-accounts-component
        :user_email="useremail"
        :scopedata="scope_data"></connected-accounts-component>

</div>

</template>

<style></style>
<script>

    export default {
        name:'ConnectCalendar',
        props:['email','token'],
        data() {
            return {
              loaded: false,
              useremail:'',
              accesstoken:'',
              scope_data: {
                  'type':'calendar',
                  'scopes':'calendar',
              }
            }

        },

        mounted() {
          this.useremail = this.email
          this.accesstoken = this.token
          this.loaded = true
        },
      computed: {

      },

        methods: {
          handleClose(tag) {
              this.bccemails.splice(this.bccemails.indexOf(tag), 1);
          },
          add_bcc_email_address() {
                 this.bccemails.push({
                   'name':this.bccemail,
                   'type':'success'
                 })
          },

        },


    }
</script>
