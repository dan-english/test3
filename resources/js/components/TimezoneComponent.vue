<template>
     <el-select v-model="selectedTimeZone" class="timezone-selector"  placeholder="Select" filterable @change="updateTimezone()" >
          <el-option
            v-for="(item, index) in timeZones"
            :key="index"
            :label="item"
            :value="item">
          </el-option>
  </el-select>
</template>

<style scoped>
.timezone-selector{
  width:100%
}
</style>
<script>

    export default {
        name:'TimeZone',
        props:['currenttimezone'],
        data() {
            return {
              loaded:false,
              timeZones: [],
              selectedTimeZone:'',
            }
        },
        watch: {},
        mounted() {
            this.timeZones = moment.tz.names();
            console.log(moment.tz.guess())

            if (this.currenttimezone) {
              this.selectedTimeZone = this.currenttimezone
            }
            else {
              this.selectedTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone
            }
        },

        methods: {
          updateTimezone(event) {
            this.$emit("timezonechanged", this.selectedTimeZone);
          }
        }
    }
</script>
