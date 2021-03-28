<template>
  <div  v-loading="loading"
           style="min-height:300px;"
        element-loading-text="Getting Message(s)..."
        element-loading-background="rgba(255, 255, 255, 1)" >

    <div v-if="loaded">
    <div class="container-fluid" id="inbox_table_header">
        <div class="row" style="padding-bottom:10px; padding-top:10px; border:1px solid #ccc; background-color:#d9d9d9">

                <div class="col-lg-6 col-xs-6">
                  <el-input placeholder="Please input" v-model="search" size="mini" style="width:50%"></el-input>
                </div>

                <div class="col-lg-6" style="text-align:right">


                       <el-select v-model="selectedValue" placeholder="Filter" size="mini">
                            <el-option
                              v-for="item in options"
                              :key="item.value"
                              :label="item.label"
                              :value="item.value">
                            </el-option>
                         </el-select>


<el-dropdown  id="inboxoptions"  size="mini">
  <el-button
      class="inboxoptions"
        size="mini"
        icon="el-icon-s-tools"
        square
        />
    <el-dropdown-menu slot="dropdown">
      <el-dropdown-item @click.prevent.native="profiile()">Connected Accounts</el-dropdown-item>
    </el-dropdown-menu>
</el-dropdown>

                </div>
        </div>
   </div>


 <el-tabs type="card" @tab-click="inbox_tab_click">
    <el-tab-pane label="Inbox" name="inbox"></el-tab-pane>
    <el-tab-pane label="Conversations" name="conversations"></el-tab-pane>
    <el-tab-pane label="Feeds" name="feeds"></el-tab-pane>
  </el-tabs>

  <el-table

       height="600"
          :data="tableData.filter(data => !search || data.subject.toLowerCase().includes(search.toLowerCase()))"

:cell-style="{padding: '0', height: '10px'}"
cell-class-name="cell_class"
          style="cursor: pointer;width:100%"

    :show-header=false
    ref="multipleTable"
    :row-class-name="tableRowClassName"
    @selection-change="handleSelectionChange">

    <el-table-column
      type="selection"
      width="45">
    </el-table-column>

    <el-table-column
      cell-class-name="cell_class"
      width="150">
            <template slot-scope="scope">
              <span v-html="unreadflag(scope.row.unread)"></span>

              <span @click="readMessage(scope.row)">{{ getToNames(scope.row.from) }}</span>
            </template>

    </el-table-column>

    <el-table-column class-name="msgdescript" style="min-width:500px">
        <template slot-scope="scope" >
          <span @click="readMessage(scope.row)" v-html="getMessageDesc(scope.row)"></span>
        </template>

    </el-table-column>
    <el-table-column width="100">
        <template slot-scope="scope" >
          <span v-html="getLeadDetails(scope.row)"></span>
        </template>
    </el-table-column>



     <el-table-column width="70" align="center" >
        <template slot-scope="scope">

          <div v-if="!scope.row.loading && !scope.row.category" class="get_category_button" @click="getCategory(scope.row)" >Get Category</div>

          <i v-if="scope.row.loading" class="nylas_spinner el-icon-loading"></i>


          <span  style="font-size:8px;text-transform:capitalize" v-if="scope.row.category" v-html="scope.row.category"></span>
        </template>
    </el-table-column>



    <el-table-column width="50px">
        <template slot-scope="scope" >
          <span @click="toggleStarred()" v-html="isStarred(scope.row)"></span>
          <span v-html="hasAttachments(scope.row)"></span>
        </template>

    </el-table-column>

  <el-table-column
      width="50">
      <template slot-scope="scope">{{ receivedDate(scope.row.date) }}</template>
    </el-table-column>
  </el-table>






</div>
  </div>

</template>

<style>

.get_category_button {
  height:18px;
  line-height:15px;
  color: #696969 !important;
  background-color: #00E5BF !important;
  border:1px solid #696969;
  border-radius:3px;
  padding-bottom:5px;
  font-size:8px!important;
  font-weight:Bold;
  width:60px;
  text-align:center
}
.get_category_button:hover {
    background-color: #696969 !important;
  color: #00E5BF !important;


}


.nylas_spinner{
  color:#00E5BF;
  font-weight:bold;
}



.cell_class div{
  font-size:11px;
}

.unread {
  font-weight:bold;
  background-color:#e9f7f3!important
}
.unread_icon {
  color:blue;
}

</style>
<script>
    import {authentication}  from '../../mixins/Authentication';

    export default {
        name:'Inbox',
        mixins: [authentication],

        data() {
            return {
              loading:true,
              tableData:[],
              allMessages:[],
              feedMessages:[],
              convoMessages:[],
              search:'',
              loaded:false,
              selectedValue:'',
             options: [
                 {
                  value: 'unread',
                  label: 'Unread'
                },
               {
                  value: 'linked_with_a_deal',
                  label: 'Linked with a deal'
               },
                         {
                  value: 'linked_with_an_open_deal',
                  label: 'Linked with an open deal'
               },
                              {
                  value: 'not_linked_with_a_deal',
                  label: 'Not linked with a deal'
               },              {
                  value: 'shared',
                  label: 'Shared'
               },              {
                  value: 'not_shared',
                  label: 'Not Shared'
               },              {
                  value: 'to_me',
                  label: 'To Me'
               },              {
                  value: 'from_exisitng_contact',
                  label: 'From an exisiting contact'
             },              {
                  value: 'only_with_attachments',
                  label: 'Only with attachments'
               },


            ]
            }
        },
        watch: {},
        mounted() {
          this.getTableData()
        },

        methods: {
          handleSelectionChange(row,index) {

          },
          tableRowClassName({row, rowIndex}) {
              if (row.unread) {
                return 'message_row unread';
              }
              return 'message_row';
         },
          unreadflag(unread) {
            if (unread) {
                return '<i class="el-icon-s-help unread_icon"></i>'
            }
          },
          getMessageDesc(row) {
            let preview = '<b>'+row.subject + '</b> '+row.snippet;

            return preview.substring(0, 100)+'...'
          },
          receivedDate (date) {
            let months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            let d = new Date(date*1000)
            let datestring = d.getDay()  + " " + months[(d.getMonth()+1)]
            return datestring
          },
          getToNames(to) {
            var a = to.map(function (person) {
              return person.name
            });

            return a.join(",");

          },
          getLeadDetails() {
            return '<i class="el-icon-s-marketing">Dan | Lead</i>'
          },
          hasAttachments(row) {

            if(row.files.length > 0) {
              return '<i class="el-icon-paperclip"></i>'
            }

          },
          toggleStarred() {
            console.log('toggle star')
          },
          isStarred(row) {
            if (row.starred) {
                return '<i class="el-icon-star-on"></i>'
            }
            else {
                return '<i class="el-icon-star-off"></i>'
            }
          },

          readMessage(message) {
            window.location = '/inbox/message/'+message.id
          },



          getTableData() {
            let app = this;
              axios.get('/inbox/messages').then((response)=>{
                    app.tableData = response.data;
                    app.allMessages = response.data;
              }).then(()=>{
                    app.loaded =true
                    app.loading=false
              app.feedMessages = app.tableData.filter(function (message) {
                      return message.category === "feed";
              });
             app.convoMessages = app.tableData.filter(function (message) {
                      return message.category === "conversation";
              });
              })


          },

          getCategory(msg) {
              let app =this
              let message = msg;
              message.loading = true
              message.category=' ';  //blank this out so the spinner shows

              axios.get('/message/category/'+message.id).then((response) => {
                      message.loading = false
                      message.category=response.data;
              }).then(()=>{
                  app.refreshEmailsWithCategories()
              });
          },

          refreshEmailsWithCategories() {
            let app = this
             app.convoMessages = app.tableData.filter(function (message) {
                      return message.category === "conversation";
              });
              app.feedMessages = app.tableData.filter(function (message) {
                      return message.category === "feed";
              });
          },


          inbox_tab_click(tab, event) {

            if(tab.name == 'feeds') {
              this.tableData = this.feedMessages;
            }

            if(tab.name == 'conversations') {
              this.tableData = this.convoMessages;
            }
              if(tab.name == 'inbox') {
              this.tableData = this.allMessages;
            }

          },
          profiile(){
            window.location = '/profile';
          }
        },


    }
</script>
