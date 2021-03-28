<template>
  <div class="container">
    <div class="demo_panel row">

      <div class="row" style="margin-left:10px;margin-right:10px;padding-left:20px;border-bottom:1px solid #ccc;padding-bottom:20px;">
         <el-tag  v-if="category" plain size="mini" >{{category}}</el-tag>
      </div>

            <div class="row" style="margin-left:10px;margin-right:10px;padding-left:20px;padding-right:20px;;border-bottom:1px solid #ccc;padding-bottom:20px;padding-top:20px;">

{{cleanconversation}}
              </div>

      <div class="row" style="margin-left:10px;margin-right:10px;padding-left:20px;padding-bottom:20px;padding-top:20px;">
        <pre v-if="signature"><code>{{signature}}</code></pre>
        <div v-if="!signature">Signature not detected</div>
      </div>


</div>
    </div>
</template>
<style>


.demo_panel {
  background-color:white;
  padding-top:30px;
  padding-bottom:30px;
  margin-bottom:30px;
  border:1px solid #ccc;


  display:block;
}
</style>
<script>
    export default {
        name:'EmailDemoPanel',
        props: ['demo_message'],
        components: {},
        data() {
            return {
              loaded:false,
              message_id:0,
              signature:' ',
              category:'',
              cleanconversation:''
            }
        },
        mounted() {
            this.message_id = this.demo_message
            this.loaded = true;
            this.getCategory()
            this.getSignatureExtract();
            this.getCleanConversation();
        },
        watch: {
          demo_message(){
            this.message_id = this.demo_message
             this.signature=' '
              this.category=''
              this.cleanconversation=''
                        this.getCategory()
            this.getSignatureExtract();
            this.getCleanConversation();
          }
        },
        methods: {
          getSignatureExtract() {
              let app=this
            if(this.message_id) {
              axios.get('/message/signature/' + app.message_id).then((response) => {
                app.signature = response.data.signature;
              })
            }

          },
          getCategory() {
              let app =this
                        if(this.message_id) {
                          axios.get('/message/category/' + app.message_id).then((response) => {
                            app.category = response.data;
                          })
                        }
          },
          getCleanConversation() {
              let app =this
                        if(this.message_id) {
                          axios.get('/message/clean/' + app.message_id).then((response) => {
                            app.cleanconversation = response.data[0]['conversation'];
                          })
                        }
          }

        }
    }
</script>
