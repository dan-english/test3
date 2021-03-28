<template>
  <div class="container-fluid">
<div  class="row" style="padding:5px;margin:5px;">

    <el-table
        ref="consoletable"
    :data="tableData"
        empty-text="Listening for API requests"
    height="600px"
    style="width: 100%">
    <el-table-column type="expand">


      <template slot-scope="props">
        <p>Method: {{ props.row.method }}</p>
        <p>Status: {{ props.row.status_code }}</p>
        <p>Time: {{ props.row.time }}</p>
        <p>Account ID: {{ props.row.account_id }}</p>
        <p>Sent: </p>
        <p>Recieved
        <pre><code>{{ props.row.response }}</code></pre></p>
      </template>
    </el-table-column>


    <el-table-column
      label="Type"
      width="150px"
      prop="type">
    </el-table-column>


    <el-table-column
      label="Endpoint"
      prop="endpoint">
    </el-table-column>

      <el-table-column
      label="Time"
      prop="time">
    </el-table-column>
  </el-table>



</div>
    <div class="row" style="text-align:center;padding-bottom:20px;">
      <div class="col-md-12">
      <el-button type="primary" plain @click="clearMessages()">Clear Messages</el-button>
        </div>
      </div>
  </div>
</template>


<script>


    export default {
        name:'ConsoleDrawer',
        data() {
            return {
               tableData: [],
               p_messages:[],
               p_channel:{}
            }
        },
        mounted() {
          let app = this

          _debug.log('Nylas Console Logger Running');
  var nylas_pusher = new Pusher('1082958fa2c8f9f47aa2', {
      cluster: 'eu'
  });
          this.p_channel = nylas_pusher.subscribe('my-channel');
          this.p_channel.bind('my-event', function(data) {
                 app.p_messages.push(JSON.stringify(data));
                _debug.apiRequest(data)
                // _debug.apiResponse(data)
                app.addTableRow(data)
          });

        },
        methods: {
          addTableRow(data){
            this.tableData = [data, ...this.tableData];
          },
          clearMessages() {
            console.log('clear messages')
          }

        }
    }

</script>

