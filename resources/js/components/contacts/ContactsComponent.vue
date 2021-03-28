<template>
    <div class="container" v-if="loaded">
        <div class="row justify-content-center">
            <div class="col-md-8">
               <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="given_name"
        label="Name"
        width="180">
      </el-table-column>
      <el-table-column
        prop="email"
        label="Email"
        width="180">
      </el-table-column>

    </el-table>

            </div>
        </div>
    </div>
</template>
<style>

</style>
<script>
    export default {
        name:'',
        props: [],
        components: {},
        data() {
            return {
              tableData:[],
              loaded:false,
            }
        },
        mounted() {
            _debug.mounted('Component');
            this.getContacts()
            this.loaded = true;
        },
        computed: {},
        watch: {},
        methods: {

          getContacts() {
            let app = this;
            axios.get('/data/contacts').then((response)=>{
              console.log(response.data)
              app.tableData = response.data
            })
          }
        }
    }
</script>
