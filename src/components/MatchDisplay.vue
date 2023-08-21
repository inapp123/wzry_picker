<template>
    <v-card class="cardbg" dark height="100%">
        <div class="match-title">
            {{matchname}}
        </div>
        <v-container style="text-align:center">
            <v-row no-gutters>
                <v-col cols="12">
                    <div class="bignumber">
                        {{scoreleft}}-{{scoreright}}
                    </div>
                </v-col>
            </v-row>
            <v-row no-gutters style="padding-top:5px;font-size:125%">
                <v-col cols="4">
                    
                    <!-- <div class="bignumber">
                        7
                    </div> -->
                    <!-- 7班 -->
                    {{teamleft}}
                </v-col>
                <v-col cols="4">

                </v-col>
                <v-col cols="4">
                    <!-- <div class="bignumber">
                        8
                    </div> -->
                    <!-- 8班 -->
                    {{teamright}}
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>

<script>
export default {
    props:{
        matchname:{
            type: String,
            required: true
        },

        teamleft:{
            type: String,
            required: true
        },
        scoreleft:{
            required: true  
        },

        teamright:{
            type: String,
            required: true
        },
        scoreright:{
            required: true  
        },
    }
}
</script>

<style>

    .match-title{
        font-size: 120%;
        font-weight: bold;
        text-align: center;
        padding-top: 5px;
    }

    .bignumber{
        font-size: 500%;
        font-family:'Courier New', Courier, monospace;
        line-height: 50px;
    }

    .cardbg{
        background: rgb(183,28,28);
        background: linear-gradient(90deg, rgba(183,28,28,1) 0%, rgba(0,0,0,1) 50%, rgba(13,71,161,1) 100%);
    }

</style>