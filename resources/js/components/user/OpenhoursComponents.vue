<template>
  <div class="" v-if="loaded">

           <div class="row row_box" >

                <div class="col-md-12">

              <div style="font-weight:Bold;font-size:14px;text-align:left;padding-bottom:15px;padding-top:15px">Open Hours</div>

    <table class="openhourstable">
                        <tr><td><el-tag class="daytag">Monday</el-tag> <el-tag class="dayplus" type="success" @click="popup('monday')"><i class="el-icon-plus"></i></el-tag></td>
                        <td>
                          <el-tag v-for="(mon, index) in openHours.monday" class="openhour" type="warning"
                          :key="index"
                          closable
                          @close="handleClose('monday', mon, index)">
                            {{ mon.start }} - {{ mon.end }}
                          </el-tag>
                        </td>
                        </tr>


                        <tr><td><el-tag class="daytag">Tuesday</el-tag><el-tag class="dayplus" type="success" @click="popup('tuesday')"><i class="el-icon-plus"></i></el-tag></td>
                         <td>
                          <el-tag v-for="(time, index) in openHours.tuesday" class="openhour" type="warning"
                          :key="index"
                          closable
                          @close="handleClose('tuesday', time, index)">
                            {{ time.start }} - {{ time.end }}
                          </el-tag>
                        </td>

                        </tr>
                        <tr><td><el-tag class="daytag">Wednesday</el-tag><el-tag class="dayplus" type="success"  @click="popup('wednesday')"><i class="el-icon-plus"></i></el-tag></td>
                        <td>
                          <el-tag v-for="(time, index) in openHours.wednesday" class="openhour" type="warning"
                          :key="index"
                          closable
                          @close="handleClose('wednesday', time, index)">
                            {{ time.start }} - {{ time.end }}
                          </el-tag>
                        </td>

                        </tr>
                        <tr><td><el-tag class="daytag">Thursday</el-tag><el-tag class="dayplus" type="success"  @click="popup('thursday')"><i class="el-icon-plus"></i></el-tag></td>
                           <td>
                          <el-tag v-for="(time, index) in openHours.thursday" class="openhour" type="warning"
                          :key="index"
                          closable
                          @close="handleClose('thursday', time, index)">
                            {{ time.start }} - {{ time.end }}
                          </el-tag>
                        </td>
                        </tr>
                        <tr><td><el-tag class="daytag">Friday</el-tag><el-tag class="dayplus" type="success"  @click="popup('friday')"><i class="el-icon-plus"></i></el-tag></td>

                          <td>
                          <el-tag v-for="(time, index) in openHours.friday" class="openhour" type="warning"
                          :key="index"
                          closable
                          @close="handleClose('friday', time, index)">
                            {{ time.start }} - {{ time.end }}
                          </el-tag>
                        </td>
                        </tr>
                        <tr><td><el-tag class="daytag" type="info">Saturday</el-tag><el-tag class="dayplus" type="success" @click="popup('saturday')"><i class="el-icon-plus"></i></el-tag></td>
  <td>
                          <el-tag v-for="(time, index) in openHours.saturday" class="openhour" type="warning"
                          :key="index"
                          closable
                          @close="handleClose('saturday', time, index)">
                            {{ time.start }} - {{ time.end }}
                          </el-tag>
                        </td>
                        </tr>
                        <tr><td><el-tag class="daytag" type="info">Sunday</el-tag><el-tag class="dayplus" type="success" @click="popup('sunday')"><i class="el-icon-plus"></i></el-tag></td>
  <td>
                          <el-tag v-for="(time, index) in openHours.sunday" class="openhour" type="warning"
                          :key="index"
                          closable
                          @close="handleClose('sunday', time, index)">
                            {{ time.start }} - {{ time.end }}
                          </el-tag>
                        </td>
                        </tr>


                      </table>


        <div class="row" style="float:right">
          <div class="col-md-12">
              <el-button @click="updateUsersOpenHours()">Save Open Hours</el-button>
          </div>
        </div>


      <el-dialog
          title="Enter Hours"
          :visible.sync="dialogVisible"
          width="30%">

            <Table>
              <tr><Td>

                 <el-time-select v-model="open.start" :picker-options="{
                format: 'HH:mm:ss',
                start: '06:00',
                step: '00:15',
                end: '19:00'
            }" placeholder="Start time">
			</el-time-select>


              </Td></tr>
              <tr>
                <Td>

              <el-time-select v-model="open.end"

                :picker-options="{
                format: 'HH:mm:ss',
                start: '06:00',
                step: '00:15',
                end: '19:00',
                minTime: open.start

            }" placeholder="End time">
			</el-time-select>

              </Td></tr>
            </Table>
              <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">Cancel</el-button>
                <el-button type="primary" @click="saveOpenHours">Add Hours</el-button>
              </span>


      </el-dialog>



                  </div>

    </div>

  </div>
</template>


<script>
    export default {
        name:'OpenhoursComponent',
        props: ['userdata'],
        data() {
            return {
              loaded:false,
              dialogVisible: false,
              user:{},
              open:{
                day:'',
                start:'',
                end:'',
              },

              openHours: {},

            }
        },
        mounted() {
            this.user = this.userdata;
            this.openHours = this.userdata['open_hours'];
            this.loaded = true;
        },

        methods: {
          popup(day) {
            this.open.day = day;
            this.dialogVisible = true;
          },
          saveOpenHours() {


            switch(this.open.day) {
               case 'monday':
                      // code block
                      if (!this.openHours['monday']) {
                        this.openHours['monday']=[];
                      }
                      this.openHours['monday'].push({start: this.open.start, end:this.open.end})
                      break;

                    case 'tuesday':
                      if (!this.openHours['tuesday']) {
                        this.openHours['tuesday']=[];
                       }
                      this.openHours['tuesday'].push({start: this.open.start, end:this.open.end})
                      break;

                    case 'wednesday':
                      if (!this.openHours['wednesday']) {
                        this.openHours['wednesday']=[];
                      }
                      this.openHours['wednesday'].push({start: this.open.start, end:this.open.end})
                      break;

                    case 'thursday':
                      if (!this.openHours['thursday']) {
                        this.openHours['thursday']=[];
                      }
                      this.openHours['thursday'].push({start: this.open.start, end:this.open.end})
                      break;
                    case 'friday':
                      if (!this.openHours['friday']) {
                        this.openHours['friday']=[];
                      }
                      this.openHours['friday'].push({start: this.open.start, end:this.open.end})
                      break;
                    case 'saturday':
                      if (!this.openHours['saturday']) {
                        this.openHours['saturday']=[];
                      }
                      this.openHours['saturday'].push({start: this.open.start, end:this.open.end})
                      break
                    case 'sunday':
                      if (!this.openHours['sunday']) {
                        this.openHours['sunday']=[];
                      }
                      this.openHours['sunday'].push({start: this.open.start, end:this.open.end})
                      break;
            }



            this.dialogVisible = false
            this.open.day=''
            this.open.start=''
            this.open.end=''

         },
          handleClose(day, tag, index) {
            this.openHours[day].splice(index,1);
            this.open.day=''
            this.open.start=''
            this.open.end=''
          },
          updateUsersOpenHours() {
            let data = this.user;
            data['open_hours'] = this.openHours

            axios.post('/profile/update/openhours', {'user_data':data})
                .then((response => {
                  console.log(response.data)
                })
            )

          }
        }
    }

</script>

