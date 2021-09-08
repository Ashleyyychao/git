<template>
  <div class="container" style="max-width: 1170px">
    <div style='width:80%;margin:auto'>
      <div class='d-flex flex-wrap'>
        <div style='width:100%;'>
          <div  class='d-flex' style='font-family: "source-han-serif-tc";font-weight: bold;font-size: 26px;'>
            <div class='pr-4 d-flex align-center'><v-img  width='45px' height='24px' :src="require('~/assets/img/agents_kind1515571234907188.jpg')"></v-img></div>
            <div>台灣地區</div>
          </div>
          <div style='font-size:26px'>一</div>
        </div>
        <div class='py-6' style='width:50%' v-for="(item, key) in taiwan" :key="key">
          <div
            style="
              font-size: 15px;
              line-height: 1.5;
              font-weight: bold;
              color: #666;
            "
          >
            {{ item.title }}
          </div>
          <table  style="table-layout: fixed; margin-bottom: 96px:empty-cells: hide;border-collapse:collapse;">
            <thead></thead>
            <tbody>
              <tr>
                <th>{{ item.title1 }}</th>
                <td>
                  <a
                    :href="'tel:' + item.phone"
                    style="text-decoration: none; color: #666"
                    >{{ item.phone }}</a
                  >
                </td>
              </tr>
              <tr>
                <th>{{ item.title2 }}</th>
                <td>{{ item.fax }}</td>
              </tr>
              <tr>
                <th>{{ item.title3 }}</th>
                <td>
                  <a
                    :href="'mailto:' + item.phone"
                    style="text-decoration: none; color: #666"
                    >{{ item.mail }}</a
                  >
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
           <div class='d-flex flex-wrap'>
        <div style='width:100%'>
          <div class='d-flex' style='font-family: "source-han-serif-tc";font-weight: bold;font-size: 26px;'>
            <div  class='pr-4 d-flex align-center'><v-img width='45px' height='24px' :src="require('~/assets/img/agents_kind1515571375423863.jpg')"></v-img></div>
           <div>中國地區</div>
          </div>
          <div style='font-size:26px'>一</div>
        </div>
        <div  :class="`${key==2 ? '' : 'py-6'}`" style='width:50%' v-for="(item, key) in china" :key="key">
          <div
            style="
              font-size: 15px;
              line-height: 1.5;
              font-weight: bold;
              color: #666;
            "
          >
            {{ item.title }}
          </div>
          <table class="table" style="table-layout: fixed; margin-bottom: 96px">
            <thead></thead>
            <tbody>
              <tr>
                <th>{{ item.title1 }}</th>
                <td>
                  <a
                    :href="'tel:' + item.phone"
                    style="text-decoration: none; color: #666"
                    >{{ item.phone }}</a
                  >
                </td>
              </tr>
              <tr>
                <th>{{ item.title2 }}</th>
                <td>{{ item.fax }}</td>
              </tr>
              <tr>
                <th>{{ item.title3 }}</th>
                <td>
                  <a
                    :href="'mailto:' + item.phone"
                    style="text-decoration: none; color: #666"
                    >{{ item.mail }}</a
                  >
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <!-- item-2 -->
      <div  class='py-6' v-for="(item, key) in item2" :key="key">
        <div class='d-flex' style='font-family: "source-han-serif-tc";font-weight: bold;font-size: 26px;'>
            <div  class='pr-4 d-flex align-center'><v-img width='45px' height='24px' :src="item.img"></v-img></div>
           <div> {{ item.country }}</div>
          </div>
        <div style='font-size:26px'>一</div>
        <div
          style="
            font-size: 15px;
            line-height: 1.5;
            font-weight: bold;
            color: #666;
          "
        >
          {{ item.title }}
        </div>
        <table class="table" style="table-layout: fixed; margin-bottom: 96px;">
          <thead></thead>
          <tbody>
            <tr>
              <th>{{ item.title1 }}</th>
              <td>
                <a
                  :href="'tel:' + item.phone"
                  style="text-decoration: none; color: #666"
                  >{{ item.phone }}</a
                >
              </td>
            </tr>
            <tr>
              <th>{{ item.title2 }}</th>
              <td>{{ item.fax }}</td>
            </tr>
            <tr>
              <th>{{ item.title3 }}</th>
              <td>
                <a
                  :href="'mailto:' + item.phone"
                  style="text-decoration: none; color: #666"
                  >{{ item.mail }}</a
                >
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      taiwan:[{
          title: "台中總部",
          title1: "電話",
          title2: "傳真",
          title3: "電子信箱",
          phone: "+886-4-22125555",
          fax: "+886-4-22121735",
          mail: "chieh@jenyuh.com.tw",
        },
        {
          title: "台北辦公室",
          title1: "電話",
          title2: "傳真",
          phone: "+886-02-29722438",
          fax: "+886-02-29738384",
        },],
      china: [
        {
          title: "華北地區 / 總代理<br/>濰坊華忠新型複合材料有限公司",
          title1: "電話",
          title2: "傳真",
          title3: "電子信箱",
          phone: "+86-536-6801788",
          fax: "+86-536-6801388",
          mail: "skyg213@presico.com.cn",
        },
        {
          title: "華中地區 / 總代理<br/>華忠金屬材料（太倉）股份有限公司",
          title1: "電話",
          title2: "傳真",
          title3: "電子信箱",
          phone: "+86-512-53563391",
          fax: "+86-512-53563393",
          mail: "presco-shc@presico.com.cn",
        },
        {
          title: `華南地區 / 總代理 <br/>普力斯科精密材料(深圳)股份有限公司`,
          title1: "電話",
          title2: "傳真",
          title3: "電子信箱",
          phone: "+86-0755-27191306",
          fax: "+86-0755-27199962",
          mail: "presicoktf@presico.com.tw",
        },
      ],
      item2: [
        {
          country: "馬來西亞地區",
          img:require("~/assets/img/agents_kind1515571448372422.jpg"),
          title: "瑞域國際銷售有限公司 / 總代理 ",
           title1: "電話",
          title2: "傳真",
          title3: "電子信箱",
          phone: "+605-2828618",
          fax: "+605-2826734",
          mail: "swiftmarketingsb@gmail.com",
        },
        {
          country: "泰國地區",
          img:require("~/assets/img/agents_kind1515571460775919.jpg"),
          title: `Global Tyler Co., Ltd / 代理商 `,
           title1: "電話",
          title3: "電子信箱",
         phone: "+66-0993-836888",
          mail: "gary@globaltyler.com",
        },
        {
          country: "新加坡地區",
          img:require("~/assets/img/agents_kind1515571417218332.jpg"),
          title: `AB Metals PTE Ltd. / 代理商`,
           title1: "電話",
          title2: "傳真",
          title3: "電子信箱",
          phone: "+65-6466-5853",
          fax: "+65-6469-5303",
          mail: "enquiry@abmetals.com.sg",
        },
        {
          country: "印尼地區",
          img:require("~/assets/img/agents_kind1515571486319360.jpg"),
          title: `AB Metals PTE Ltd. / 代理商`,
           title1: "電話",
          title2: "傳真",
          title3: "電子信箱",
          phone: "+65-6466-5853",
          fax: "+65-6469-5303",
          mail: "enquiry@abmetals.com.sg",
        },
      ],
    };
  },
};
</script>
<style scoped>
th{
  border-top: 1px solid #ffc005;
  border-bottom: 1px solid #ffc005;
}
td{
  border-top: 1px solid #e9e9e9;
  border-bottom: 1px solid #e9e9e9;
}
tr{
  height:52px
}

table{
  empty-cells: hide;
  border-collapse:collapse;
}

</style>
