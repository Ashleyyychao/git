<template>
  <div class='bgm'>
    <div class="container" style="max-width: 1170px; width: 100%;padding-bottom:150px">
      <div  class='py-15' style="max-width: 780px; margin: auto;">
        <div class="text-center py-10">
          <div style='font-family: "source-han-serif-tc";margin-bottom: 22px;font-weight: bold;font-size: 26px;'>有任何問題?</div>
          <div style='font-size: 16px;line-height: 22px;color: #333;'>
            若您有任何問題或需求，請填寫以下問題項目，我們將會有專人儘快與您聯繫。謝謝！
          </div>
        </div>
        <div class='py-5' style="position: relative">
          <input type="text" />
          <p>
            詢問價錢
          </p>
        </div>
        <div class='py-5' style="position: relative">
          <input type="text" />
          <p>
            <span style='color: #ffc005;margin-right: 1px;font-size:12px;position: absolute;left: -10px;'>*</span>公司名稱
          </p>
        </div>
          <div class='py-5' style="position: relative">
          <input type="text" />
          <p >
            <span style='color: #ffc005;margin-right: 1px;font-size:12px;position: absolute;left: -10px;'>*</span>聯絡人
          </p>
        </div>
          <div class='py-5' style="position: relative">
          <input type="number" />
          <p
            >
            <span style='color: #ffc005;margin-right: 1px;font-size:12px;position: absolute;left: -10px;'>*</span>電話
          </p>
        </div>
          <div class='py-5' style="position: relative">
          <input type="mail" />
          <p
            >
            <span style='color: #ffc005;margin-right: 1px;font-size:12px;position: absolute;left: -10px;'>*</span>電子信箱
          </p>
        </div>
        <div class='py-5' style="position: relative">
          <textarea></textarea>
          <p
            style="position: absolute;left: 20px;bottom: 152px;font-size: 16px;  " >
            <span style='color: #ffc005;margin-right: 1px;font-size:12px;position: absolute;left: -10px;'>*</span>問題與建議
          </p>
        </div>
        <div class='py-5' style="position: relative">
          <input type="number" />
          <p >
            <span style='color: #ffc005;margin-right: 1px;font-size:12px;position: absolute;left: -10px;'>*</span>驗證碼
          </p>
        </div>
        <div> <input type="submit" value="送出" style='background: #ffc005;border-color: #ffc005;color: #fff;font-size: 18px;padding-left: 0;'/></div>
        
      </div>
    </div>
  </div>
</template>
<style scoped>
.bgm{
  background-image: url("../../assets/img/contactbg.jpg");
  background-size: cover;
}
textarea{
  background: none;
  border: 1px solid #8e8e8e;
  width: 100%;
  height: 188px;
  padding: 50px 28px 20px 28px;
}
input {
  background: none;
  border: 1px solid #8e8e8e;
  width: 100%;
  height: 50px;
  padding-left: 100px;
}
input:focus ,textarea:focus{
  outline: none;
}
p{
position: absolute;
left: 20px;
bottom: 15px;
font-size: 16px;
}
</style>