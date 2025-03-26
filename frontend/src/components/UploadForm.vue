<template>
  <div>
    <h2>Создание 3D-абажура</h2>
    <form @submit.prevent="generateModel">
      <label for="height">Высота (мм):</label>
      <input type="number" v-model="height" required />

      <label for="diameter">Диаметр (мм):</label>
      <input type="number" v-model="diameter" required />

      <button type="submit">Создать 3D-модель</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      height: 150,
      diameter: 100,
    };
  },
  methods: {
    async generateModel() {
      const response = await fetch("http://127.0.0.1:8001/generate_model", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ height: this.height, diameter: this.diameter }),
      });
      const data = await response.json();
      alert("3D-модель создана: " + data.file_path);
    },
  },
};
</script>
