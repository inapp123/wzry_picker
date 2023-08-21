<template>
  <v-card max-width="120px" height="100%" dark :color="heroColor">
    <v-img 
      :src="heroImg"
    ></v-img>
    
    <div style="text-align:center">
      {{heroname == ""? "待选择": heroname}}
    </div>
  </v-card>
</template>

<script>


export default {
  props:{
    heroname:{
      type: String,
      required: true
    },
    isRedSide:{
      type: Boolean,
      required: true
    }
  },
  computed:{
    heroImg(){
      if(this.heroname == "ban"){
        return require('@/assets/ban.svg');
      }
      else if(this.heroname != ""){
        return require('@/assets/' + this.heroname + '.jpg');
      }
      else{
        return require('@/assets/empty.svg');
      }
      
    },
    heroColor(){
      if(this.isRedSide){
        return 'red darken-4';
      }else{
        return 'blue darken-4';
      }
    }
  }
}
</script>

<style>

</style>