<template>
  <div v-if="loaded">


<div class="lead_panel" v-for="lead in deals_leads" >
        <el-button @click="dealSummary()">dsf</el-button>
          <div @click="dealSummary(lead.id)" class="lead_title">{{lead.title}}</div>
          <div class="lead_owner">{{lead.owner}}</div>
          <div><i class="el-icon-user-solid"></i> ${{lead.value}}</div>
      </div>
  </div>
</template>

<style>
.lead_panel {
  background-color:white;
  border:1px solid #ccc;
  margin:2px;
  padding:2px;
}

.lead_title {
  font-weight:bold;
}
.lead_owner {
  font-size:10px;
}

</style>
<script>


    export default {
        name:'DealsLeads',
        props:[],
        data() {
            return {
              loaded: false,
              deals_leads:[],
            }

        },

        mounted() {
          this.getLeadDeals();
          this.loaded = true

        },

        methods: {

          getLeadDeals() {
            let app=this
            axios.get('/deals/leads').then((response)=>{
              console.log(response.data)
              app.deals_leads = response.data;
            })
          },
          dealSummary(deal_id) {
            console.log('load summary')
            window.location = '/deal/'+deal_id
          }
        },


    }
</script>
