// src/main.ts
import { createApp } from 'vue';
import App from './App.vue';
import { createVuetify } from 'vuetify';
import { router } from './router'; // Import the router
import 'vuetify/styles'; // Import Vuetify styles
import '@mdi/font/css/materialdesignicons.css'; // Material Design Icons

import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import { createPinia } from 'pinia';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate';

const vuetify = createVuetify({
    theme: {
      defaultTheme: 'dark', // Set the default theme to dark
      themes: {
        dark: {
          dark: true,
          colors: {
            background: '#121212', // Dark background color
            surface: '#1e1e1e', // Dark surface color
            primary: '#BB86FC', // Customize your primary color
            secondary: '#03DAC6', // Customize your secondary color
            error: '#CF6679', // Error color
            success: '#03DAC5', // Success color
          },
        },
      },
    },
    components,
    directives,
  });

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate); // Register the persistence plugin

createApp(App)
  .use(router)  // Use the router
  .use(pinia)
  .use(vuetify) // Use Vuetify
  .mount('#app');
