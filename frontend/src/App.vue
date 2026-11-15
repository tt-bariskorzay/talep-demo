<script setup>
import { onMounted, reactive, ref } from "vue";

const ortam = ref({ ortam: "…", surum: "…" });
const talepler = ref([]);
const form = reactive({ baslik: "", aciklama: "" });
const hata = ref("");

async function yukle() {
  ortam.value = await (await fetch("/api/ortam/")).json();
  talepler.value = (await (await fetch("/api/talepler/")).json()).talepler;
}

async function gonder() {
  hata.value = "";
  const yanit = await fetch("/api/talepler/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(form),
  });
  if (!yanit.ok) {
    hata.value = (await yanit.json()).hata || "Talep kaydedilemedi";
    return;
  }
  form.baslik = "";
  form.aciklama = "";
  await yukle();
}

onMounted(yukle);
</script>

<template>
  <header :class="['bant', ortam.ortam]">
    <strong>{{ ortam.ortam.toUpperCase() }} ortamı</strong>
    <span>sürüm {{ ortam.surum }}</span>
  </header>

  <main>
    <h1>Yeni talep</h1>
    <form @submit.prevent="gonder">
      <label>Başlık <input v-model="form.baslik" required /></label>
      <label>Açıklama <textarea v-model="form.aciklama" rows="3"></textarea></label>
      <p v-if="hata" class="hata">{{ hata }}</p>
      <button type="submit">Talebi kaydet</button>
    </form>

    <h2>Son talepler</h2>
    <ul>
      <li v-for="t in talepler" :key="t.id">
        <strong>{{ t.baslik }}</strong>
        <span v-if="t.aciklama"> · {{ t.aciklama }}</span>
      </li>
    </ul>
  </main>
</template>

<style>
body { margin: 0; font-family: Arial, sans-serif; background: #FBFCFD; color: #002855; }
.bant { display: flex; justify-content: space-between; padding: 12px 24px; color: #fff; background: #4A5B70; font-size: 18px; }
.bant.test { background: #0082CA; }
.bant.prod { background: #D42B1C; }
main { max-width: 640px; margin: 0 auto; padding: 24px; }
form { display: flex; flex-direction: column; gap: 14px; background: #EEF3F7; padding: 20px; }
label { display: flex; flex-direction: column; gap: 6px; font-weight: 600; font-size: 18px; }
input, textarea, select { font: inherit; font-weight: 400; padding: 8px; border: 1px solid #C9D3DD; }
button { align-self: flex-start; font: inherit; padding: 10px 18px; background: #002855; color: #fff; border: 0; cursor: pointer; }
.hata { color: #D42B1C; margin: 0; }
li { padding: 6px 0; font-size: 18px; }
</style>
