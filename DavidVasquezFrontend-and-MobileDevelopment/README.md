# Aplicaciones de Consulta de Clima - React, Angular y Vue

Este proyecto contiene tres aplicaciones web que demuestran las funcionalidades de consulta de clima implementadas en los principales frameworks de frontend: React, Angular y Vue.js.

## 🌤️ Funcionalidades de Clima

Cada aplicación incluye:

- **Búsqueda por ciudad**: Ingresa el nombre de cualquier ciudad del mundo
- **Datos meteorológicos completos**: Temperatura, sensación térmica, humedad, viento, presión
- **Iconos del clima**: Visualización gráfica de las condiciones meteorológicas
- **Historial de búsquedas**: Acceso rápido a ciudades buscadas anteriormente
- **Manejo de errores**: Mensajes informativos para ciudades no encontradas
- **Diseño responsivo**: Funciona perfectamente en dispositivos móviles y desktop
- **Interfaz en español**: Todas las descripciones y mensajes en español

## 🚀 Configuración

### 1. Obtener API Key de OpenWeatherMap

Para que las aplicaciones funcionen correctamente, necesitas obtener una API key gratuita:

1. Ve a [OpenWeatherMap](https://openweathermap.org/)
2. Crea una cuenta gratuita
3. Ve a "API Keys" en tu perfil
4. Copia tu API key

### 2. Configurar API Key en cada aplicación

#### React App
```typescript
// En react-app/src/App.tsx
const API_KEY = 'TU_API_KEY_AQUI'; // Reemplaza con tu API key
```

#### Angular App
```typescript
// En angular-app/src/app/app.ts
private readonly API_KEY = 'TU_API_KEY_AQUI'; // Reemplaza con tu API key
```

#### Vue App
```javascript
// En vue-app/src/App.vue
const API_KEY = 'TU_API_KEY_AQUI' // Reemplaza con tu API key
```

## 📦 Instalación y Ejecución

### React App
```bash
cd react-app
npm install
npm start
```
La aplicación estará disponible en: http://localhost:3000

### Angular App
```bash
cd angular-app
npm install
ng serve
```
La aplicación estará disponible en: http://localhost:4200

### Vue App
```bash
cd vue-app
npm install
npm run dev
```
La aplicación estará disponible en: http://localhost:5173

## 🎨 Características de cada Framework

### React
- **Hooks**: useState, useEffect para manejo de estado
- **Componentes funcionales**: Arquitectura moderna de React
- **TypeScript**: Tipado estático para mayor robustez
- **Manejo de eventos**: Formularios y botones interactivos

### Angular
- **Signals**: Reactividad moderna de Angular 17+
- **TypeScript**: Framework completamente tipado
- **Componentes**: Arquitectura basada en componentes
- **Dependency Injection**: Sistema robusto de inyección de dependencias

### Vue.js
- **Composition API**: API moderna de Vue 3
- **Reactivity**: Sistema reactivo automático
- **Directivas**: v-model, v-if, v-for para manipulación del DOM
- **SFC**: Single File Components con template, script y estilos

## 🔧 Tecnologías Utilizadas

### React
- React 18
- TypeScript
- CSS Modules
- Fetch API

### Angular
- Angular 17
- TypeScript
- Signals
- Fetch API

### Vue
- Vue 3
- Composition API
- Scoped CSS
- Fetch API

## 📱 Diseño Responsivo

Todas las aplicaciones incluyen:
- Diseño mobile-first
- Breakpoints para tablets y desktop
- Interfaz adaptativa
- Elementos táctiles optimizados

## 🌍 API de Clima

Las aplicaciones utilizan la API de OpenWeatherMap que proporciona:
- Datos meteorológicos en tiempo real
- Información de más de 200,000 ciudades
- Soporte para múltiples idiomas
- Iconos meteorológicos
- Datos de calidad profesional

## 🎯 Ejemplos de Uso

1. **Búsqueda básica**: Escribe "Madrid" y presiona buscar
2. **Historial**: Las ciudades buscadas aparecen como botones para acceso rápido
3. **Información detallada**: Ver temperatura, humedad, viento y presión
4. **Iconos del clima**: Visualización gráfica de las condiciones actuales

## 🔒 Seguridad

- Las API keys deben mantenerse privadas
- No subir las keys a repositorios públicos
- Usar variables de entorno en producción
- Implementar rate limiting para evitar abuso de la API

## 📄 Licencia

Este proyecto es educativo y está disponible bajo la licencia MIT.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📞 Soporte

Si tienes problemas o preguntas:
- Revisa la documentación de cada framework
- Verifica que tu API key sea válida
- Asegúrate de que todas las dependencias estén instaladas

---

¡Disfruta explorando las diferentes implementaciones de consulta de clima en React, Angular y Vue! 🌤️ 