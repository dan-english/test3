<template>
  <div v-if="loaded">
    <div class="container-fluid" id="deal_header">


      <div class="row ">
          <div class="col-md-3" style="text-align:left">
                    <h1 class="deal_title">{{deal.title}}</h1>
          </div>
          <div class="col-md-9" style="text-align:right">


                <el-dropdown style="padding:10px;float:right">

                  <el-button
                       @click.stop="a()"
                        size="mini"
                        icon="el-icon-more"
                        square

                        style="margin-left: 5px;" />
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item>Duplicate</el-dropdown-item>

                  </el-dropdown-menu>
                </el-dropdown>

                    <div style="background-color:red;color:white;border:1px solid #ccc;width:45px;text-align:center;margin:5px;float:right">
      Lost
    </div>
                    <div style="background-color:Green;color:white;border:1px solid #ccc;width:45px;text-align:center;margin:5px;float:right">
      Won
    </div>
            </div>
      </div>


      <div class="row" style="padding-bottom:10px;">

          <span class="deal_value">$100,000</span>
          <span class="deal_add_products">Add Products</span>
          <span class="deal_contact"><i class="el-icon-s-custom"></i> Jonny Hutch</span>
          <span class="deal_org"><i class="el-icon-office-building"></i> Jonny's Bar</span>
        </div>

<el-progress :text-inside="true" :stroke-width="26" :percentage="10"></el-progress>

            <div class="row" style="padding-left:10px;">


              <div class="col-md-3">
              {{deal.stage}}
              </div>

            </div>


    </div>
</div>
</template>

<style>
#deal_header{
  background-color:white;
}
.deal_header {
  background-color:white;
  border:1px solid #ccc;
  margin:2px;
  padding:2px;
}

.deal_title {
  font-size:23px;
  color:rgb(49, 122, 226);
  text-transform:Capitalize;
  font-family:"Source Sans Pro", sans-serif;
  padding-top:5px;
  padding-left:10px;
}
.deal_value{
  padding-left:30px;
  font-size:15px;
}
.deal_add_products {
  font-size:12px;
  padding-left:10px;
  line-height:15px;
}
.deal_contact{
  font-size:12px;
  padding-left:10px;
}
.deal_org {
  padding-left:10px;
}


</style>
<script>

    export default {
        name:'DealsLeads',
        props:['deal_data'],
        data() {
            return {
              loaded: false,
              deal:{}
            }

        },

        mounted() {
          console.log(this.deal_data)
        this.deal = this.deal_data
          this.loaded = true

        },

        methods: {




        },


    }
</script>
