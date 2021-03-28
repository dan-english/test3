<template>

   <div class="row row_box" >
          <div class="col-md-12">
              <div style="font-weight:Bold;font-size:14px;text-align:left;padding-bottom:15px;padding-top:15px">Interface</div>

              <ul class="interfacelist">
                    <li><el-checkbox  v-model="checked1">Open details panel after creating a new item</el-checkbox></li>
                    <li style="padding-left:20px;"><el-checkbox v-model="checkedDeal">Deal</el-checkbox></li>
                    <li style="padding-left:20px;"><el-checkbox v-model="checkePerson">Person</el-checkbox></li>
                    <li style="padding-left:20px;"><el-checkbox v-model="checked4">Organization</el-checkbox></li>
                    <li><el-checkbox v-model="checked5">Convert phone numbers to US phone number format</el-checkbox></li>
                    <li><el-checkbox v-model="checked6">Open new tab when clicking on email links</el-checkbox></li>
                    <li><el-checkbox v-model="checked7">Show celebratory animation after every won deal</el-checkbox></li>

                </ul>
          </div>

     </div>
</template>
<style>

</style>

<script>
    export default {
        name:'InterfaceOptionsComponent',
        props: [],
        data() {
            return {
              checked1:true,
              checkedDeal:false,
              checkePerson:true,
              checked4:false,
              checked5:false,
              checked6:false,
              checked7:true,
            }
        },
        mounted() {},
        methods: {}
    }

</script>

