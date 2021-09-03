<template>
 <div class='container'>
     <v-row>
     <div class='d-flex' style='width:100vw'>
         <div class='py-3 px-10 ' style='width:20%;text-align:center'>關於我們</div>
         <div class='py-3 px-10' style='width:20%;text-align:center'>最新消息</div>
         <div class='py-3 px-10' style='width:20%;text-align:center'>產品介紹</div>
         <div class='py-3 px-10' style='width:20%;text-align:center'>創新技術</div>
         <div class='py-3 px-10' style='width:20%;text-align:center'>聯絡我們</div>
         <div class='py-3 px-10' style='width:20%;text-align:center'>客戶專區</div>
     </div>
     </v-row>
 </div>
</template>

<script>
export default {
  data: () => ({
    items: [
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me" },
      { title: "Click Me 2" },
    ],
  }),
};
</script>
