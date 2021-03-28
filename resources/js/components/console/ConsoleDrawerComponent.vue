<template>
  <div>
<div id="consoledrawer">

  <el-dropdown style="float:right" size="mini">

  <el-button
      class="consoleoptions"
        size="mini"
        icon="el-icon-more"
        square
         />
    <el-dropdown-menu slot="dropdown">
      <el-dropdown-item @click.prevent.native="hideConsoleDrawer()"> Hide Console</el-dropdown-item>
    </el-dropdown-menu>
</el-dropdown>
    <el-table
    :data="tableData"
    height="187px"
    empty-text="Listening for API requests"
    style="width: 100%;">
    <el-table-column type="expand">


      <template slot-scope="props">
        <p>Method: {{ props.row.method }}</p>
        <p>Status: {{ props.row.status_code }}</p>
        <p>Time: {{ props.row.time }}</p>
        <p>Account ID: {{ props.row.account_id }}</p>
        <p>Sent: </p>
        <p>Recieved
          <pre><code>{{ props.row.response }}</code></pre>
        </p>
      </template>
    </el-table-column>


    <el-table-column
      label="Type"
      prop="type">
    </el-table-column>


    <el-table-column
      label="Endpoint"
      prop="endpoint">
    </el-table-column>

      <el-table-column
      label="Account Email"
      prop="endpoint">
    </el-table-column>
  </el-table>

  <div style="margin-top: 20px"><!--spacing--></div>

</div>

      <el-dropdown  id="showconsole"  size="mini">

  <el-button
      class="consoleoptions"
        size="mini"
        icon="el-icon-more"
        square
        />
    <el-dropdown-menu slot="dropdown">
      <el-dropdown-item @click.prevent.native="showConsoleDrawer()">Show Console</el-dropdown-item>
    </el-dropdown-menu>
</el-dropdown>

    </div>
</template>
<style>
#consoledrawer {
  position:fixed;
  bottom:0;
  left:0;
  background-color:white;
  border-top:3px solid #696969;
  padding-top:10px;
  padding-bottom:50px;
  margin-bottom:100px;
  height:100px;
  width:100%;
  z-index:1000;
}
#showconsole {
  color:#696969!important;
  background-color:#00E5BF!important;
  border-radius:0;
  position: fixed;
  bottom: 0;
  right: 0;
}
.consoleoptions {
  color:#696969!important;
  background-color:#00E5BF!important;
border-radius:0;

}
</style>

<script>
  var nylas_pusher = new Pusher('1082958fa2c8f9f47aa2', {
      cluster: 'eu'
  });

    export default {
        name:'ConsoleDrawer',
        data() {
            return {
              tableData: [],
              p_messages:[],
              p_channel:{},


            }
        },
        mounted() {
          _debug.log('Nylas Console Logger Running');
          let app = this

          const getCookieValue = (name) => (
             document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || ''
          )
          let showConsole=getCookieValue('console');
            (showConsole === '1' ? this.showConsoleDrawer() : this.hideConsoleDrawer())


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
            // this.tableData.push(data)
          },
          hideConsoleDrawer() {
            let elem = document.getElementById('consoledrawer')
            elem.style.display = "none";
            this.setCookie('0')

          },
          showConsoleDrawer(){
             let elem = document.getElementById('consoledrawer')
             elem.style.display = "block";
             this.setCookie('1')

          },
          setCookie(value) {
            let date = new Date();
            date.setTime(date.getTime() + (7 * 24 * 60 * 60 * 1000));
            document.cookie = "console="+value+";path=/; expires=" + date.toUTCString()
          }
        }
    }

</script>

