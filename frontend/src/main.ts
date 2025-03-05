import { createApp } from 'vue';
import App from './App.vue';
import { router } from './router';  // 确保使用正确的导入路径
import { createPinia } from 'pinia';
import './assets/index.css';


import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import './styles/index.css';



const app = createApp(App);

const pinia = createPinia();
app.use(pinia);
app.use(ElementPlus);
app.use(router);

app.mount('#app');


