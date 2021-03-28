<template>
<div style="min-height:300px;"
        v-loading="loading"
        element-loading-text="Getting Message(s)..."
        element-loading-background="rgba(255, 255, 255, 1)" >

  <div v-if="loaded">

      <div class="el-row message_header" >
              <div class="el-col-sm-18 el-col-md-19 el-col-lg-20">
                <h3 class="thread_subject">{{thread_subject}}</h3>
              </div>
              <div class="el-col-md-4 hidden-xs-only" style="text-align:right;padding-right:5px;padding-top:5px">
                    <el-button plain v-if="!clean" size="mini"  style="font-size:9px" type="success" @click="seeClean()">Clean Thread</el-button>
              </div>
      </div>


    <div class="el-row ">
    <email-demo-panel-component v-if="!clean && demo_message_id==1"
                                :signature="show_signature"
                                :clean="clean_conversation"
                                :demo_message="demo_message_id">

    </email-demo-panel-component>
</div>

    <div  class="latest_message" @click="showLatestMessage()">
        <div class="el-row">
            <div class="el-col-xs-2" >
                <el-avatar class="thread_avatar" size="small" icon="el-icon-user-solid" style="float:left;font-size:10px"></el-avatar>
            </div>
            <div class="el-col-sm-23">
                  <div class="el-row" style="padding-top:1px;">

                        <div class="from el-col-sm-20" style="padding-top:4px;" >
                          <span class="from_name">{{latest_message.from[0].name}}</span><span v-if="!clean" class="from_email">{{latest_message.from[0].email}}</span>
                        </div>

                         <div class="whenheader el-col-sm-4">
                          {{receivedDate (latest_message.date) }}

                           <i style="font-size:12px" class="el-icon-star-off"></i>
                           <img @click.stop="showComposer()" class="reply_image" style="width:20px;;margin-bottom:5px;" src="/images/reply.png">

<el-dropdown>
<div class="category_button"   @click.stop="a()">Feed</div>
<el-dropdown-menu slot="dropdown" >

    <el-dropdown-item @click.prevent.native="categoryFeedback()" style="font-size:10px;
    padding:2px;margin:3px;height:12px;padding-bottom:10px;
    line-height:6px">Give Feedback</el-dropdown-item>



  </el-dropdown-menu>
</el-dropdown>


<el-dropdown>

<div class="more_button" @click.stop="a()">
  <i class="el-icon-more"></i>
</div>

  <el-dropdown-menu slot="dropdown">
        <el-dropdown-item @click.prevent.native="showSignature()" style="font-size:10px;
    padding:2px;margin:3px;height:12px;padding-bottom:10px;
    line-height:6px">Show Signature</el-dropdown-item>

  </el-dropdown-menu>

</el-dropdown>

                        </div>


                    </div>



                  <div class="el-col-md-21">

                    <!--message preview -->
                  <div class="snippet" v-if="!latest_expanded && !clean">
                    {{ shorterSnippet(latest_message.snippet)  }}
                  </div>
                  <div class="snippet" v-if="!latest_expanded && clean">
                    {{ shorterSnippet(latest_message.conversation)  }}
                  </div>
                   <!-- //message preview -->


              <div v-if="latest_expanded" v-html="emailContent(latest_message)" style="font-size:10px;padding-top:10px;"></div>

               <div style="padding-top:5px;" v-if="latest_expanded">
                   <el-tag size="mini" style="font-size:8px;margin:3px;" plain v-if="file.filename" v-for="(file, index) in latest_message.files" :key="index">{{file.filename}}</el-tag>
               </div>

<div v-if="signature" class="row" style="padding-top:10px;border-top:1px solid #ccc;">
  <div class="col-md-6">
                    <div>
                      <pre>{{signature}}</pre>

                    </div>
</div>
  <div class="col-md-6">
                    <div >
                      <pre>{{signature_contacts}}</pre>

                    </div>
    </div>



</div>

            </div>
            </div>
       </div>
  </div>
      <div  class="thread_counter" v-if="thread_count > 1">
             <el-avatar class="thread_message_count" size="small">{{thread_count}}</el-avatar>
             <div style="border-top:1px solid #ccc;height:10px;width:100%;margin-top:10px;">&nbsp;</div>
        </div>

      <div v-for="(message, index) in messages" @click="showMessage(message.id)" >
              <div class="message" v-if="index > 0">
                  <div  class="el-row">
                                <div class="el-col-xs-2" >
                                    <el-avatar class="thread_avatar" size="small" icon="el-icon-user-solid" style="float:left;font-size:10px"></el-avatar>
                                </div>

                                <div class="el-col-sm-23">
                                              <div class="el-row">
                                                    <div class="from el-col-sm-20" >
                                                      <span class="from_name">{{message.from[0].name}}</span><span v-if="!clean" class="from_email">{{message.from[0].email}}</span>
                                                    </div>

                                                     <div class="whenheader el-col-sm-4">
                                                      {{receivedDate (message.date) }}
                                                    </div>
                                                </div>

                                                <div class="el-col-md-21">

                                                        <div class="snippet" v-if="active_msg != message.id && !clean">
                                                          {{ shorterSnippet(message.snippet)  }}
                                                        </div>
                                                        <div class="snippet" v-if="active_msg != message.id && clean">
                                                          {{ shorterSnippet(message.conversation)  }}
                                                        </div>


                                                        <div v-if="active_msg == message.id" v-html="emailContent(message)" style="font-size:10px;padding-top:10px;"></div>


                                                </div>
                                </div>


                  </div>
              </div>
        </div>

      <div class="el-row thread_footer" >
      <div v-if="clean" class="el-row " style="padding-top:10px;font-style:italic;font-size:9px">
        <i class="el-icon-info" style="color:orange"></i>&nbsp;Each message has been processed by the <a href="https://docs.nylas.com/docs/neural-clean-conversation-guide" target="_blank">clean conversation</a> endpoint
      </div>
      </div>




  </div><!--loaded-->

<div v-if="1==2">
  <nylas-composer visible="false" id="bfccecff-dbac-4464-9187-3de7aa16cc45"></nylas-composer>

</div>


</div><!--loading-->
</template>
<style>

.reply_image{

}
.reply_image:hover{
  cursor:pointer;
}
.more_button{
    height:20px;
  line-height:10px;
  width:20px;

  font-size:11px;
  border-radius:10px;
  text-align:center;
  margin:5px;
  padding-top:4px;

     color:#E6A23C;
  background-color:#fdf6ec;
  border:1px solid #f5dab1;
}
.el-dropdown-menu {
  padding:3px;
  margin-top:1px!important;
}
.el-dropdown-menu__item:focus, .el-dropdown-menu__item:hover{
  background-color:white!important;
}
.category_button {
  height:20px;
  line-height:10px;

  font-size:11px;
  border-radius:3px;
  text-align:center;
  margin:5px;
  padding-top:4px;
  padding-left:10px;
  padding-right:10px;
     color:#E6A23C;
  background-color:#fdf6ec;
  border:1px solid #f5dab1;
}


.thread_message_count {
  background-color:white;
  color:#b9babb;
  position:absolute;
  top:-15px;
  left:10px;
  z-index:100;
  border:1px solid #ccc;
  padding-top:5px;
  line-height:16px;

}
.thread_counter {
  width:100%;
  margin-top:3px;
  position:relative;
}
.thread_footer {
  background-color:white;
  border:1px solid #ccc;

}


.thread_avatar {
  height:16px;
  width:16px;
  line-height:16px;
  margin:5px;
  color:blue;
  background-color:rgba(49, 122, 226, 0.16)
}
.thread_subject {
  font-size:15px;
  padding:10px;
  margin:0px;
}
.message_header {
  border:1px solid #ccc;
  background-color:white;
  margin-bottom:5px;
}

.latest_message, .message {
  background-color:white;
  border-left:1px solid #ccc;
  border-right:1px solid #ccc;
  border-top:1px solid #ccc;
  padding-bottom:5px;
  padding-top:5px;
}
.latest_message {
  border-bottom:1px solid #ccc;
}

.whenheader, .from, .snippet {
  font-size:9px;
  color:#747678;
  font-family: 'Source Sans Pro', sans-serif;
}
.whenheader {
  font-size:8px;
  text-align:right;
}

.from_name {
  color:#000;
  font-weight:bold;
  font-size:11px;
}
.from_email {
  font-size:10px;
  padding-left:5px;
  color:#000;
}
</style>
<script>

    export default {
        name:'Message',
        props:['message_data'],
        data() {
            return {

              loaded:false,
              loading:true,
              message_id:'',  //this should be the message id on the url (ie the selected message)
              tmpdata:[], //this should hold all messages but unsorted by date

              messages:[],
              latest_message:{},
              latest_expanded:false,
              thread:{},
              thread_count:0, //total number of messages in this thread
              neural:false,  //flag to determine if this has been through the clean endpoint
              active_msg:0,

              demo_message_id:0,
              show_signature:false,
              show_clean_conversation:false,

              signature:'',
              signature_contacts:'',

            }
        },

        mounted() {
            this.message_id = this.message_data.id;
            this.clean = this.message_data.clean;
            this.getMessageData()
        },

        methods: {
          a(){},

          showComposer(){
              const composer = document.getElementById('bfccecff-dbac-4464-9187-3de7aa16cc45')
                // to show the composer (if attribute "visible" is set to false)
              // composer.open();

              // to close the composer
              // composer.close();
          },
          showSignature() {
              this.getSignatureExtract()
          },

          shorterSnippet(snippet) {
                  return snippet.substring(0, 150)+'...'
                } ,
          receivedDate (date) {
                let months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
                let d = new Date(date*100)
                let datestring = d.getDay()  + " " + months[(d.getMonth()+1)]
                return datestring
          },
          showLatestMessage() {
                    this.latest_expanded = !this.latest_expanded
                    if(this.latest_expanded) {
                      this.demo_message_id = this.message_id;

                    }
                },
          showMessage(message_id) {
              if(this.active_msg == message_id) {
                  this.active_msg = 0
              }
              else {
                  this.active_msg = message_id;
                  this.demo_message_id = message_id;
              }
          },


                emailContent(message) {
                  if(message.conversation) {
                    return message.conversation
                  }
                  return message.body
                },
                seeClean() {
                        window.open( '/inbox/message/clean/' + this.message_id, "_blank", "noopener");
                },


                getMessageData() {
                  let app = this;
                  let url = '/data/inbox/thread/';

                  if(app.clean) {
                    url = '/data/inbox/thread/clean/'
                  }

                      axios.get(url+app.message_id).then((response) => {
                        let data = response.data;

                        app.messages = _.sortBy(data.messages, [function(o) { return o.date; }]).reverse();
                        app.latest_message = app.messages[0]
                        app.account_id = app.latest_message['account_id']

                        app.thread_subject = data.subject
                        app.thread_count = app.messages.length

                        app.active_msg=app.message_id

                        if(app.thread_count == 1) {
                            app.latest_expanded = true;
                        }

                      }).then(()=>{
                          app.loaded=true;
                          app.loading=false;
                      })
                },

                 getSignatureExtract() {
            console.log('get sig')
                    let app=this
                      if(this.active_msg) {
                        axios.get('/message/signature/' + app.active_msg).then((response) => {
                          app.signature = response.data.signature;
                          app.signature_contacts = response.data.contacts;

                          console.log(response.data)
                          console.log('done')
                        })
                      }

                },

                getCategory() {
                    let app =this
                    if(this.active_msg) {
                      axios.get('/message/category/' + app.active_msg).then((response) => {
                        app.category = response.data;
                      })
                 }
                },
                categoryFeedback() {
                  let app = this
                  if (app.active_msg) {
                    axios.post('/message/category/feedback', {'message_id':app.active_msg, 'account_id':app.account_id}).then((response) => {
                      app.category = response.data;
                      console.log(response.data)
                    })
                  }
                }
        }
    }
</script>
