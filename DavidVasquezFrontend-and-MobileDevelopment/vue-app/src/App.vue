<script setup>
import { ref, computed, onMounted, watch } from 'vue'

// Estado reactivo con ref
const count = ref(0)
const inputValue = ref('')
const showInfo = ref(false)
const items = ref(['Vue.js', 'Reactivity', 'Components', 'Directives'])
const selectedFramework = ref('vue')

// Weather app reactive data
const city = ref('')
const weatherData = ref(null)
const loading = ref(false)
const error = ref(null)
const searchHistory = ref([])
const searchCount = ref(0)
const apiKey = ref('')
const showApiInstructions = ref(false)

// Computed property
const doubleCount = computed(() => count.value * 2)

// Frameworks para comparación
const frameworks = ref({
  react: {
    name: 'React',
    type: 'UI Library',
    company: 'Meta (Facebook)',
    language: 'JavaScript + JSX',
    learning: 'Medium',
    pros: ['Virtual DOM', 'Large ecosystem', 'Flexibility', 'React Native'],
    cons: ['Not a complete framework', 'Complex ecosystem learning curve'],
    code: `// React - Hooks
const [count, setCount] = useState(0);
const increment = () => setCount(count + 1);

return (
  <div>
    <p>Counter: {count}</p>
    <button onClick={increment}>+</button>
  </div>
);`
  },
  vue: {
    name: 'Vue.js',
    type: 'Progressive Framework',
    company: 'Community',
    language: 'JavaScript + Templates',
    learning: 'Low',
    pros: ['Low learning curve', 'Progressive adoption', 'Intuitive syntax', 'Official ecosystem'],
    cons: ['Less corporate backing', 'Smaller community'],
    code: `<!-- Vue - Composition API -->
&lt;script setup&gt;
const count = ref(0);
const increment = () => count.value++;
&lt;/script&gt;

&lt;template&gt;
  &lt;div&gt;
    &lt;p&gt;Counter: {{ count }}&lt;/p&gt;
    &lt;button @click="increment"&gt;+&lt;/button&gt;
  &lt;/div&gt;
&lt;/template&gt;`
  },
  angular: {
    name: 'Angular',
    type: 'Complete Framework',
    company: 'Google',
    language: 'TypeScript',
    learning: 'High',
    pros: ['Complete framework', 'TypeScript', 'Powerful CLI', 'Dependency injection'],
    cons: ['High learning curve', 'More verbose', 'Less flexible'],
    code: `// Angular - Signals
@Component({
  selector: 'app-counter',
  template: \`
    <div>
      <p>Counter: {{ count() }}</p>
      <button (click)="increment()">+</button>
    </div>
  \`
})
export class CounterComponent {
  count = signal(0);
  increment() {
    this.count.update(value => value + 1);
  }
}`
  }
})

// Computed para el framework actual
const currentFramework = computed(() => frameworks.value[selectedFramework.value])

// Métodos
const increment = () => {
  count.value++
}

const decrement = () => {
  count.value--
}

const toggleInfo = () => {
  showInfo.value = !showInfo.value
}

const addItem = () => {
  if (inputValue.value.trim()) {
    items.value.push(inputValue.value)
    inputValue.value = ''
  }
}

const removeItem = (index) => {
  items.value.splice(index, 1)
}

const selectFramework = (framework) => {
  selectedFramework.value = framework
}

// Lifecycle hook
onMounted(() => {
  console.log('Vue component mounted')
})

// Watcher
watch(count, (newValue, oldValue) => {
  console.log(`Counter changed from ${oldValue} to ${newValue}`)
})

// Weather app methods
const API_URL = 'https://api.openweathermap.org/data/2.5/weather'

const fetchWeather = async (cityName) => {
  if (!apiKey.value.trim()) {
    error.value = 'Please enter your OpenWeatherMap API key first'
    return
  }

  if (searchCount.value >= 5) {
    error.value = 'You have reached the maximum of 5 searches per session. Reload the page to search more.'
    return
  }

  loading.value = true
  error.value = null
  searchCount.value++

  try {
    const response = await fetch(
      `${API_URL}?q=${cityName}&appid=${apiKey.value}&units=metric&lang=en`
    )
    
    if (!response.ok) {
      if (response.status === 401) {
        throw new Error('Invalid API key. Please check your OpenWeatherMap API key.')
      }
      throw new Error('City not found')
    }
    
    const data = await response.json()
    weatherData.value = data
    
    // Agregar a historial
    if (!searchHistory.value.includes(cityName)) {
      searchHistory.value = [cityName, ...searchHistory.value.slice(0, 4)]
    }
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Error getting data'
    weatherData.value = null
  } finally {
    loading.value = false
  }
}

const handleSearch = (event) => {
  event.preventDefault()
  if (city.value.trim()) {
    fetchWeather(city.value.trim())
  }
}

const handleHistoryClick = (cityName) => {
  city.value = cityName
  fetchWeather(cityName)
}

const getWeatherIcon = (iconCode) => {
  return `https://openweathermap.org/img/wn/${iconCode}@2x.png`
}

const getWeatherDescription = (weatherId) => {
  const descriptions = {
    200: 'Thunderstorm with light rain',
    201: 'Thunderstorm with rain',
    202: 'Thunderstorm with heavy rain',
    300: 'Light drizzle',
    301: 'Drizzle',
    500: 'Light rain',
    501: 'Moderate rain',
    502: 'Heavy rain',
    600: 'Light snow',
    601: 'Snow',
    602: 'Heavy snow',
    700: 'Mist',
    800: 'Clear sky',
    801: 'Few clouds',
    802: 'Scattered clouds',
    803: 'Broken clouds',
    804: 'Overcast clouds'
  }
  return descriptions[weatherId] || 'Unknown condition'
}
</script>

<template>
  <div class="app">
    <header class="header">
      <h1>🟢 Vue.js - Educational Framework</h1>
      <p>Application that demonstrates the main features of Vue.js</p>
    </header>

    <main class="main">
      <div class="framework-info">
        <h2>What is Vue.js?</h2>
        <ul>
          <li>🎯 Progressive JavaScript framework</li>
          <li>⚡ Automatic reactivity</li>
          <li>📦 Component system</li>
          <li>🎨 Built-in directives (v-if, v-for, v-model)</li>
          <li>🛠️ Composition API and Options API</li>
          <li>🚀 Gradual adoption - from small component to complete SPA</li>
        </ul>
      </div>

      <div class="feature-card">
        <h3>Vue.js Features</h3>
        
        <div class="feature-item">
          <h4>🎯 Reactivity (ref)</h4>
          <p>Counter: {{ count }}</p>
          <p>Double: {{ doubleCount }}</p>
          <button @click="increment">+</button>
          <button @click="decrement">-</button>
        </div>

        <div class="feature-item">
          <h4>📝 v-model (Two-way binding)</h4>
          <input 
            v-model="inputValue"
            type="text" 
            placeholder="Write something..."
          />
          <p>Text: {{ inputValue }}</p>
          <button @click="addItem">Add item</button>
        </div>

        <div class="feature-item">
          <h4>🔄 v-if and v-show</h4>
          <button @click="toggleInfo">
            {{ showInfo ? 'Hide' : 'Show' }} information
          </button>
          <div v-if="showInfo" class="info-box">
            <p>This text appears/disappears using v-if</p>
            <p>Vue handles reactivity automatically</p>
          </div>
        </div>

        <div class="feature-item">
          <h4>📋 v-for (Reactive list)</h4>
          <ul class="item-list">
            <li v-for="(item, index) in items" :key="index">
              {{ item }}
              <button @click="removeItem(index)" class="remove-btn">×</button>
            </li>
          </ul>
        </div>
      </div>

      <div class="weather-app">
        <h3>🌤️ Weather App</h3>
        
        <div class="api-instructions">
          <h4>📋 How to use this Weather App:</h4>
          <ol>
            <li>Get your free API key from <a href="https://openweathermap.org/api" target="_blank" rel="noopener noreferrer">OpenWeatherMap</a></li>
            <li>Sign up for a free account</li>
            <li>Go to "My API keys" section</li>
            <li>Copy your API key and paste it below</li>
            <li>Enter any city name and search!</li>
          </ol>
          <button 
            @click="showApiInstructions = !showApiInstructions"
            class="toggle-instructions-btn"
          >
            {{ showApiInstructions ? 'Hide' : 'Show' }} API Key Instructions
          </button>
        </div>

        <div v-if="showApiInstructions" class="api-key-section">
          <h4>🔑 Enter your OpenWeatherMap API Key:</h4>
          <div class="api-input-group">
            <input
              v-model="apiKey"
              type="password"
              placeholder="Paste your API key here..."
              class="api-key-input"
            />
            <button 
              @click="apiKey = ''"
              class="clear-api-btn"
              title="Clear API key"
            >
              🗑️
            </button>
          </div>
          <p class="api-note">
            <strong>Note:</strong> Your API key is stored only in your browser and is not sent to any server except OpenWeatherMap.
          </p>
        </div>
        
        <form @submit="handleSearch" class="weather-form">
          <div class="input-group">
            <input
              v-model="city"
              type="text" 
              placeholder="Enter any city name in the world..."
              class="city-input"
              :disabled="!apiKey.trim()"
            />
            <button type="submit" :disabled="loading || !city.trim() || !apiKey.trim()">
              {{ loading ? '🔍 Searching...' : '🔍 Search' }}
            </button>
          </div>
          <p class="venezuela-info">
            🌎 You can search any city in the world.<br/>
            Remaining searches: {{ 5 - searchCount }}
            <span v-if="!apiKey.trim()" class="api-warning"><br/>⚠️ Please enter your API key first</span>
          </p>
        </form>

        <div v-if="searchHistory.length > 0" class="search-history">
          <h4>📋 Search history:</h4>
          <div class="history-buttons">
            <button
              v-for="(cityName, index) in searchHistory"
              :key="index"
              @click="handleHistoryClick(cityName)"
              class="history-btn"
            >
              {{ cityName }}
            </button>
          </div>
        </div>

        <div v-if="error" class="error-message">
          ❌ {{ error }}
        </div>

        <div v-if="weatherData" class="weather-card">
          <div class="weather-header">
            <h4>{{ weatherData.name }}, {{ weatherData.sys.country }}</h4>
            <img 
              :src="getWeatherIcon(weatherData.weather[0].icon)" 
              :alt="weatherData.weather[0].description"
              class="weather-icon"
            />
          </div>
          
          <div class="weather-info">
            <div class="temperature">
              <span class="temp-value">{{ Math.round(weatherData.main.temp) }}°C</span>
              <span class="temp-feels">Feels like: {{ Math.round(weatherData.main.feels_like) }}°C</span>
            </div>
            
            <div class="weather-description">
              {{ getWeatherDescription(parseInt(weatherData.weather[0].icon.slice(0, -1))) }}
            </div>
            
            <div class="weather-details">
              <div class="detail-item">
                <span class="detail-label">💧 Humidity:</span>
                <span class="detail-value">{{ weatherData.main.humidity }}%</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">🌬️ Wind:</span>
                <span class="detail-value">{{ weatherData.wind.speed }} m/s</span>
              </div>
              <div class="detail-item">
                <span class="detail-label">📊 Pressure:</span>
                <span class="detail-value">{{ weatherData.main.pressure }} hPa</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="comparison-section">
        <h3>🔄 Framework Comparison</h3>
        
        <div class="framework-selector">
          <button 
            :class="{ active: selectedFramework === 'react' }"
            @click="selectFramework('react')"
          >
            React
          </button>
          <button 
            :class="{ active: selectedFramework === 'vue' }"
            @click="selectFramework('vue')"
          >
            Vue.js
          </button>
          <button 
            :class="{ active: selectedFramework === 'angular' }"
            @click="selectFramework('angular')"
          >
            Angular
          </button>
        </div>

        <div class="framework-details">
          <div class="framework-info">
            <h4>{{ currentFramework.name }}</h4>
            <div class="info-grid">
              <div><strong>Type:</strong> {{ currentFramework.type }}</div>
              <div><strong>Company:</strong> {{ currentFramework.company }}</div>
              <div><strong>Language:</strong> {{ currentFramework.language }}</div>
              <div><strong>Learning curve:</strong> {{ currentFramework.learning }}</div>
            </div>
          </div>

          <div class="pros-cons">
            <div class="pros">
              <h5>✅ Advantages</h5>
              <ul>
                <li v-for="(pro, index) in currentFramework.pros" :key="index">
                  {{ pro }}
                </li>
              </ul>
            </div>
            <div class="cons">
              <h5>❌ Disadvantages</h5>
              <ul>
                <li v-for="(con, index) in currentFramework.cons" :key="index">
                  {{ con }}
                </li>
              </ul>
            </div>
          </div>

          <div class="code-example">
            <h5>💻 Code Example</h5>
            <pre>{{ currentFramework.code }}</pre>
          </div>
        </div>
      </div>

      <div class="code-example">
        <h3>Vue.js Code Example</h3>
        <pre>
&lt;script setup&gt;
import { ref, computed } from 'vue'

const count = ref(0)
const doubleCount = computed(() => count.value * 2)

const increment = () => {
  count.value++
}
&lt;/script&gt;

&lt;template&gt;
  &lt;div&gt;
    &lt;p&gt;Counter: {{ count }}&lt;/p&gt;
    &lt;p&gt;Double: {{ doubleCount }}&lt;/p&gt;
    &lt;button @click="increment"&gt;Increment&lt;/button&gt;
  &lt;/div&gt;
&lt;/template&gt;</pre>
      </div>
    </main>
  </div>
</template>

<style scoped>
.app {
  min-height: 100vh;
  background: linear-gradient(135deg, #42b883 0%, #35495e 100%);
  color: white;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.header {
  padding: 2rem;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  text-align: center;
}

.header h1 {
  margin: 0;
  font-size: 2.5rem;
  font-weight: 700;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.header p {
  margin: 1rem 0 0 0;
  font-size: 1.2rem;
  opacity: 0.9;
}

.main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  display: grid;
  gap: 2rem;
  grid-template-columns: 1fr 1fr;
}

.framework-info {
  background: rgba(255, 255, 255, 0.1);
  padding: 2rem;
  border-radius: 15px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  text-align: left;
}

.framework-info h2 {
  margin-top: 0;
  color: #42b883;
  font-size: 1.8rem;
}

.framework-info ul {
  list-style: none;
  padding: 0;
}

.framework-info li {
  margin: 1rem 0;
  padding: 0.5rem 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 1.1rem;
}

.feature-card {
  background: rgba(255, 255, 255, 0.1);
  padding: 2rem;
  border-radius: 15px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  text-align: left;
}

.feature-card h3 {
  margin-top: 0;
  color: #42b883;
  font-size: 1.8rem;
  text-align: center;
}

.feature-item {
  margin: 1.5rem 0;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.feature-item h4 {
  margin: 0 0 1rem 0;
  color: #42b883;
  font-size: 1.3rem;
}

.feature-item button {
  background: #42b883;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  margin: 0.5rem;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.3s;
}

.feature-item button:hover {
  background: #369870;
}

.feature-item input {
  width: 100%;
  padding: 0.5rem;
  margin: 0.5rem 0;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  background: rgba(255, 255, 255, 0.9);
  color: #333;
}

.info-box {
  background: rgba(255, 255, 255, 0.1);
  padding: 1rem;
  border-radius: 8px;
  margin-top: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.item-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.item-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem;
  margin: 0.25rem 0;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 5px;
}

.remove-btn {
  background: #e74c3c !important;
  color: white;
  border: none;
  border-radius: 50%;
  width: 25px;
  height: 25px;
  cursor: pointer;
  font-size: 1rem;
  line-height: 1;
}

.remove-btn:hover {
  background: #c0392b !important;
}

/* Estilos para la sección de comparación */
.comparison-section {
  grid-column: 1 / -1;
  background: rgba(255, 255, 255, 0.1);
  padding: 2rem;
  border-radius: 15px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  text-align: left;
}

.comparison-section h3 {
  margin-top: 0;
  color: #42b883;
  font-size: 1.8rem;
  text-align: center;
}

.framework-selector {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.framework-selector button {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border: 2px solid rgba(255, 255, 255, 0.3);
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.3s;
}

.framework-selector button:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.5);
}

.framework-selector button.active {
  background: #42b883;
  color: white;
  border-color: #42b883;
}

.framework-details {
  display: grid;
  gap: 2rem;
  grid-template-columns: 1fr 1fr;
}

.framework-info h4 {
  margin-top: 0;
  color: #42b883;
  font-size: 1.5rem;
  text-align: center;
}

.info-grid {
  display: grid;
  gap: 0.5rem;
  margin-top: 1rem;
}

.info-grid div {
  padding: 0.5rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 5px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.pros-cons {
  display: grid;
  gap: 1rem;
}

.pros, .cons {
  background: rgba(255, 255, 255, 0.05);
  padding: 1rem;
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.pros h5 {
  color: #4CAF50;
  margin-top: 0;
  font-size: 1.2rem;
}

.cons h5 {
  color: #f44336;
  margin-top: 0;
  font-size: 1.2rem;
}

.pros ul, .cons ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.pros li, .cons li {
  margin: 0.5rem 0;
  padding: 0.25rem 0;
  font-size: 0.9rem;
}

.code-example {
  grid-column: 1 / -1;
  background: rgba(0, 0, 0, 0.3);
  padding: 2rem;
  border-radius: 15px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.code-example h3 {
  margin-top: 0;
  color: #42b883;
  font-size: 1.8rem;
  text-align: center;
}

.code-example h5 {
  margin-top: 0;
  color: #42b883;
  font-size: 1.3rem;
  text-align: center;
}

.code-example pre {
  background: #1e1e1e;
  color: #d4d4d4;
  padding: 1.5rem;
  border-radius: 8px;
  overflow-x: auto;
  text-align: left;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
  line-height: 1.4;
  border: 1px solid #333;
}

/* Estilos para la aplicación de clima */
.weather-app {
  grid-column: 1 / -1;
  background: rgba(255, 255, 255, 0.1);
  padding: 2rem;
  border-radius: 15px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  text-align: center;
}

.weather-app h3 {
  margin-top: 0;
  color: #42b883;
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
}

/* Estilos para las instrucciones de API */
.api-instructions {
  background: rgba(255, 255, 255, 0.05);
  padding: 1.5rem;
  border-radius: 10px;
  margin-bottom: 1.5rem;
  text-align: left;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.api-instructions h4 {
  color: #42b883;
  margin-top: 0;
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

.api-instructions ol {
  margin: 0;
  padding-left: 1.5rem;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.6;
}

.api-instructions li {
  margin: 0.5rem 0;
}

.api-instructions a {
  color: #42b883;
  text-decoration: none;
  font-weight: 600;
}

.api-instructions a:hover {
  text-decoration: underline;
}

.toggle-instructions-btn {
  background: #42b883;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  cursor: pointer;
  font-size: 0.9rem;
  margin-top: 1rem;
  transition: background 0.3s;
}

.toggle-instructions-btn:hover {
  background: #369870;
}

.api-key-section {
  background: rgba(255, 255, 255, 0.05);
  padding: 1.5rem;
  border-radius: 10px;
  margin-bottom: 1.5rem;
  text-align: left;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.api-key-section h4 {
  color: #42b883;
  margin-top: 0;
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

.api-input-group {
  display: flex;
  gap: 0.5rem;
  align-items: center;
  margin-bottom: 1rem;
}

.api-key-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  background: rgba(255, 255, 255, 0.9);
  color: #333;
  font-family: 'Courier New', monospace;
}

.api-key-input:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(66, 184, 131, 0.5);
}

.clear-api-btn {
  background: #f44336;
  color: white;
  border: none;
  padding: 0.75rem;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.3s;
}

.clear-api-btn:hover {
  background: #d32f2f;
}

.api-note {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
  margin: 0;
  font-style: italic;
}

.api-warning {
  color: #ff9800;
  font-weight: 600;
}

.weather-form {
  margin-bottom: 1.5rem;
}

.input-group {
  display: flex;
  gap: 1rem;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}

.city-input {
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  background: rgba(255, 255, 255, 0.9);
  color: #333;
  min-width: 250px;
}

.city-input:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(66, 184, 131, 0.5);
}

.city-input:disabled {
  background: rgba(255, 255, 255, 0.5);
  cursor: not-allowed;
}

.weather-form button {
  background: #42b883;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  transition: background 0.3s;
}

.weather-form button:hover:not(:disabled) {
  background: #369870;
}

.weather-form button:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.venezuela-info {
  color: #42b883;
  font-size: 0.95rem;
  margin-top: 0.5rem;
  text-align: center;
  font-weight: 600;
  line-height: 1.5;
}

.search-history {
  margin: 1.5rem 0;
  text-align: left;
}

.search-history h4 {
  color: #42b883;
  margin-bottom: 0.5rem;
}

.history-buttons {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.history-btn {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 0.5rem 1rem;
  border-radius: 20px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.3s;
}

.history-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.5);
}

.error-message {
  background: rgba(244, 67, 54, 0.2);
  color: #ffebee;
  padding: 1rem;
  border-radius: 8px;
  margin: 1rem 0;
  border: 1px solid rgba(244, 67, 54, 0.3);
}

.weather-card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  padding: 2rem;
  margin-top: 1.5rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.weather-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.weather-header h4 {
  margin: 0;
  color: #42b883;
  font-size: 1.5rem;
}

.weather-icon {
  width: 80px;
  height: 80px;
}

.weather-info {
  text-align: left;
}

.temperature {
  margin-bottom: 1rem;
}

.temp-value {
  font-size: 3rem;
  font-weight: bold;
  color: #42b883;
  display: block;
}

.temp-feels {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.8);
  display: block;
  margin-top: 0.5rem;
}

.weather-description {
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  color: rgba(255, 255, 255, 0.9);
}

.weather-details {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}

.detail-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.detail-label {
  font-weight: 600;
  color: rgba(255, 255, 255, 0.9);
}

.detail-value {
  font-weight: bold;
  color: #42b883;
}

@media (max-width: 768px) {
  .main {
    grid-template-columns: 1fr;
    padding: 1rem;
  }
  
  .header h1 {
    font-size: 2rem;
  }
  
  .header p {
    font-size: 1rem;
  }

  .framework-details {
    grid-template-columns: 1fr;
  }

  .framework-selector {
    flex-direction: column;
    align-items: center;
  }

  .framework-selector button {
    width: 100%;
    max-width: 200px;
  }

  .input-group {
    flex-direction: column;
    align-items: stretch;
  }

  .city-input {
    min-width: auto;
  }

  .api-input-group {
    flex-direction: column;
    align-items: stretch;
  }

  .weather-header {
    flex-direction: column;
    text-align: center;
  }

  .weather-details {
    grid-template-columns: 1fr;
  }
}
</style>
