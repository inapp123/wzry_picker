<template>
  <v-app class="no_scroll">
    <div class="render_area">
      <!-- <hero-display
      :heroname="'牛魔'"
      :isRedSide="true" />
      <hero-display
      :heroname="''"
      :isRedSide="true" /> -->

      <v-expand-transition>
        <div v-show="display" style="margin:10px">
          <v-container style="max-width: 999999px">
            <v-row no-gutters>
              <v-col cols="4">
                <v-container style="padding: 0px">
                  <v-row no-gutters>
                    <v-col
                      cols="2"
                      v-for="(hname, idx) in red_ban"
                      :key="'red-ban-' + idx"
                    >
                      <hero-display :heroname="hname" :isRedSide="true" />
                    </v-col>
                    <v-col cols="2">
                      <hero-display :heroname="'ban'" :isRedSide="true" />
                    </v-col>
                  </v-row>
                </v-container>
              </v-col>
              <v-col cols="4">
                <!-- spacer -->
              </v-col>
              <v-col cols="4">
                <v-container style="padding: 0px">
                  <v-row no-gutters>
                    <v-col cols="2"> </v-col>
                    <v-col cols="2">
                      <hero-display :heroname="'ban'" :isRedSide="false" />
                    </v-col>
                    <v-col
                      cols="2"
                      v-for="(hname, idx) in blue_ban"
                      :key="'blue-ban-' + idx"
                    >
                      <hero-display :heroname="hname" :isRedSide="false" />
                    </v-col>
                  </v-row>
                </v-container>
              </v-col>
            </v-row>
            <v-row no-gutters>
              <v-col
                cols="1"
                v-for="(hname, idx) in red_hero_stat"
                :key="'red-' + idx"
              >
                <hero-display :heroname="hname" :isRedSide="true" />
              </v-col>
              <v-col cols="2">
                <match-display
                  :matchname="matchname"
                  :teamleft="teamleft"
                  :scoreleft="scoreleft"
                  :teamright="teamright"
                  :scoreright="scoreright"
                />
              </v-col>
              <v-col
                cols="1"
                v-for="(hname, idx) in blue_hero_stat"
                :key="'blue-' + idx"
              >
                <hero-display :heroname="hname" :isRedSide="false" />
              </v-col>
            </v-row>
          </v-container>
        </div>
      </v-expand-transition>
    </div>

    <v-main>
      <v-container>
        <v-row>
          <v-col cols="4">
            <v-card>
              <v-card-title>给红队的</v-card-title>

              <v-card-text>
                <v-autocomplete
                  v-model="red_picked"
                  :items="all_hero"
                  dense
                  chips
                  label="红队英雄选择"
                  deletable-chips
                  multiple
                ></v-autocomplete>

                <v-autocomplete
                  v-model="red_banned"
                  :items="all_hero"
                  dense
                  chips
                  label="红队禁用选择"
                  deletable-chips
                  multiple
                ></v-autocomplete>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col cols="2">
            <v-card>
              <v-card-title>中间的的编辑-1</v-card-title>

              <v-card-text>
                <v-text-field
                  v-model="matchname"
                  label="比赛名称"
                ></v-text-field>

                <v-text-field
                  v-model="teamleft"
                  label="红队队名"
                ></v-text-field>

                <v-text-field
                  v-model="teamright"
                  label="蓝队队名"
                ></v-text-field>

              </v-card-text>

              <v-card-actions>
                <v-btn @click="display = !display" text>{{display?"隐藏":"显示"}}</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>

          <v-col cols="2">
            <v-card>
              <v-card-title>中间的的编辑-2</v-card-title>
              <v-card-text>
                <v-text-field
                  v-model="scoreleft"
                  label="红队大比分"
                ></v-text-field>

                <v-text-field
                  v-model="scoreright"
                  label="蓝队大比分"
                ></v-text-field>
              </v-card-text>
              <v-divider />
              <v-card-actions>
                <v-btn @click="clearhero()" text>重开</v-btn>
                <v-btn @click="switchteam()" text>交换</v-btn>

              </v-card-actions>
            </v-card>
          </v-col>

          <v-col cols="4">
            <v-card>
              <v-card-title>给蓝队的</v-card-title>

              <v-card-text>
                <v-autocomplete
                  v-model="blue_picked"
                  :items="all_hero"
                  dense
                  chips
                  label="蓝队英雄选择"
                  multiple
                  deletable-chips
                ></v-autocomplete>

                <v-autocomplete
                  v-model="blue_banned"
                  :items="all_hero"
                  dense
                  chips
                  label="蓝队禁用选择"
                  multiple
                  deletable-chips
                ></v-autocomplete>
              </v-card-text>
            </v-card>
          </v-col>

        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import HeroDisplay from "./components/HeroDisplay.vue";
import MatchDisplay from "./components/MatchDisplay.vue";

export default {
  name: "App",

  components: {
    HeroDisplay,
    MatchDisplay,
  },

  data: () => ({
    all_hero: ["亚连", "姬小满", "莱西奥", "赵怀真", "海月", "戈娅", "桑启", "暃", "金蝉", "云缨", "艾琳", "司空震", "澜", "夏洛特", "阿古朵", "蒙恬", "镜", "蒙犽", "鲁班大师", "西施", "马超", "曜", "云中君", "瑶", "盘古", "猪八戒", "嫦娥", "上官婉儿", "李信", "沈梦溪", "伽罗", "盾山", "司马懿", "孙策", "元歌", "米莱狄", "狂铁", "弈星", "裴擒虎", "杨玉环", "公孙离", "明世隐", "女娲", "梦奇", "苏烈", "百里玄策", "百里守约", "铠", "鬼谷子", "干将莫邪", "东皇太一", "大乔", "黄忠", "诸葛亮", "哪吒", "太乙真人", "蔡文姬", "雅典娜", "杨戬", "成吉思汗", "钟馗", "虞姬", "李元芳", "张飞", "刘备", "后羿", "牛魔", "孙悟空", "亚瑟", "橘右京", "娜可露露", "不知火舞", "张良", "花木兰", "兰陵王", "王昭君", "韩信", "刘邦", "姜子牙", "露娜", "程咬金", "安琪拉", "貂蝉", "关羽", "老夫子", "武则天", "项羽", "达摩", "狄仁杰", "马可波罗", "李白", "宫本武藏", "典韦", "曹操", "甄姬", "夏侯惇", "周瑜", "吕布", "芈月", "白起", "扁鹊", "孙膑", "钟无艳", "阿轲", "高渐离", "刘禅", "庄周", "鲁班七号", "孙尚香", "嬴政", "妲己", "墨子", "赵云", "小乔", "廉颇"],
    red_picked: [],
    red_banned: [],
    blue_picked: [],
    blue_banned: [],
    red_hero_stat: ["", "", "", "", ""],
    blue_hero_stat: ["", "", "", "", ""],
    red_ban: ["", "", "", ""],
    blue_ban: ["", "", "", ""],
    teamleft: "班",
    scoreleft: "0",
    teamright: "班",
    scoreright: "0",
    matchname:"决赛",
    display:false
  }),

  methods:{
    clearhero(){
      this.red_picked = []
      this.red_banned = []
      this.blue_picked = []
      this.blue_banned = []
    },
    switchteam(){
      let temp = this.teamleft
      this.teamleft = this.teamright
      this.teamright = temp

      temp = this.scoreleft
      this.scoreleft = this.scoreright
      this.scoreright = temp
    }
  },

  watch:{
    red_picked: {
      handler: function(){
        for (let index = 0; index < 5; index++) {
          if(this.red_picked[index]){
            this.red_hero_stat[index] = this.red_picked[index]
          }
          else{
            this.red_hero_stat[index] = ""
          }
        }
      },
      deep: true
    },
    blue_picked: {
      handler: function(){
        for (let index = 0; index < 5; index++) {
          if(this.blue_picked[index]){
            this.blue_hero_stat[4-index] = this.blue_picked[index]
          }
          else{
            this.blue_hero_stat[4-index] = ""
          }
        }
      },
      deep: true
    },
    red_banned: {
      handler: function(){
        for (let index = 0; index < 4; index++) {
          if(this.red_banned[index]){
            this.red_ban[index] = this.red_banned[index]
          }
          else{
            this.red_ban[index] = ""
          }
        }
      },
      deep: true
    },
    blue_banned: {
      handler: function(){
        for (let index = 0; index < 4; index++) {
          if(this.blue_banned[index]){
            this.blue_ban[3-index] = this.blue_banned[index]
          }
          else{
            this.blue_ban[3-index] = ""
          }
        }
      },
      deep: true
    },
  }
};
</script>

<style>
.render_area {
  background-color: rgb(0, 255, 0);
  height: 350px;
  width: 100%;
  padding: 20px;
  z-index: 99999;
}

.no_scroll {
}
</style>
