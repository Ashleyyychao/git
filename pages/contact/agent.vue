<template>
  <div class="container" style='max-width:1170px'>
    <div>
      <div></div>
      <div></div>
      <div>台灣地區</div>
      <div>一</div>
      <div v-for="(item, key) in items" :key="key">
        <div>{{ item.title }}</div>
        <table class="table">
          <thead></thead>
          <tbody>
            <tr>
              <th>{{ item.title1 }}</th>
              <td>{{ item.phone }}</td>
            </tr>
            <tr>
              <th>{{ item.title2 }}</th>
              <td>{{ item.fax }}</td>
            </tr>
            <tr>
              <th>{{ item.title3 }}</th>
              <td>{{ item.mail }}</td>
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
      items: [
        {
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
          title2: "電子信箱",
          phone: "+886-02-29722438",
          fax: "+886-02-29738384",
        },
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
         {
          title: "Global Tyler Co., Ltd / 代理商",
          title1: "電話",
          title3: "電子信箱",
          phone: "+66-0993-836888",
          mail: "gary@globaltyler.com",
        },
          {
         title: `AB Metals PTE Ltd. / 代理商`,
          title1: "電話",
          title2: "傳真",
          title3: "電子信箱",
          phone: "+65-6466-5853",
          fax: "+65-6469-5303",
          mail: "enquiry@abmetals.com.sg",
        },
        {
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
