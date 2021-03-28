<template>
<div class="sidebar" v-if="loaded">

<el-button class="mail_button" size="mini" title="Compose" @click="goCompose()"> <i class="el-icon-edit"></i></el-button>
<el-button class="mail_button"size="mini" title="Inbox" @click="goInbox()"> <i class="el-icon-folder"></i></el-button>
<el-button class="mail_button"size="mini" title="Drafts"><i class="el-icon-tickets"></i></el-button>
<el-button class="mail_button"size="mini" title="Send"> <i class="el-icon-position"></i></el-button>
<el-button class="mail_button"size="mini"> <i class="el-icon-bangzhu"></i></el-button>

</div>
</template>
<style>
.sidebar {
  height: 100%;


}

.mail_button{
  margin-left:30px!important;
  margin-bottom:2px;
}


</style>
<script>

    export default {
        name:'MailSideBar',
        props:['data'],
        data() {
            return {
              loaded:false,
              active_msg:'',
              original_msg_requested:'',
              latest_message:{},
              latest_expanded:false,
              messages:[],
              thread_count:0,
              neural:0,
            }
        },
        watch: {},
        mounted() {
          this.loaded = true


        },

        methods: {
          goInbox() {
            window.location = '/inbox'
          },
          goCompose() {
            window.location = '/compose'
          }

        }
    }
</script>
