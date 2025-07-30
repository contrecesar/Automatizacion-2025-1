import { Component, signal, computed, effect } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  // Estado reactivo con signals
  count = signal(0);
  inputValue = signal('');
  showInfo = signal(false);
  items = signal(['Angular', 'Signals', 'Components', 'Directives']);
  selectedFramework = signal<'react' | 'vue' | 'angular'>('angular');

  // Weather app reactive data
  city = signal('');
  weatherData = signal<any>(null);
  loading = signal(false);
  error = signal<string | null>(null);
  searchHistory = signal<string[]>([]);
  searchCount = signal(0);
  apiKey = signal('');
  showApiInstructions = signal(false);

  // Computed properties
  doubleCount = computed(() => this.count() * 2);

  // Frameworks para comparación
  frameworks = signal({
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
<script setup>
const count = ref(0);
const increment = () => count.value++;
</script>

<template>
  <div>
    <p>Counter: {{ count }}</p>
    <button @click="increment">+</button>
  </div>
</template>`
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
  });

  // Computed para el framework actual
  currentFramework = computed(() => this.frameworks()[this.selectedFramework()]);

  // API URL
  API_URL = 'https://api.openweathermap.org/data/2.5/weather';

  // Math object for template
  Math = Math;
  parseInt = parseInt;

  // Ejemplo de código para mostrar en el template
  codeExample = `
@Component({
  selector: 'app-example',
  template: \`
    <div>
      <p>Counter: {{ count() }}</p>
      <p>Double: {{ doubleCount() }}</p>
      <button (click)="increment()">Increment</button>
    </div>
  \`
})
export class ExampleComponent {
  count = signal(0);
  doubleCount = computed(() => this.count() * 2);

  increment() {
    this.count.update(value => value + 1);
  }
}`;

  constructor() {
    // Effect para logging
    effect(() => {
      console.log(`Counter changed to: ${this.count()}`);
    });
  }

  // Métodos
  increment() {
    this.count.update(value => value + 1);
  }

  decrement() {
    this.count.update(value => value - 1);
  }

  toggleInfo() {
    this.showInfo.update(value => !value);
  }

  addItem() {
    if (this.inputValue().trim()) {
      this.items.update(items => [...items, this.inputValue()]);
      this.inputValue.set('');
    }
  }

  removeItem(index: number) {
    this.items.update(items => items.filter((_, i) => i !== index));
  }

  onInputChange(event: Event) {
    const target = event.target as HTMLInputElement;
    this.inputValue.set(target.value);
  }

  selectFramework(framework: 'react' | 'vue' | 'angular') {
    this.selectedFramework.set(framework);
  }

  // Weather app methods
  async fetchWeather(cityName: string) {
    if (!this.apiKey().trim()) {
      this.error.set('Please enter your OpenWeatherMap API key first');
      return;
    }

    if (this.searchCount() >= 5) {
      this.error.set('You have reached the maximum of 5 searches per session. Reload the page to search more.');
      return;
    }

    this.loading.set(true);
    this.error.set(null);
    this.searchCount.update(value => value + 1);

    try {
      const response = await fetch(
        `${this.API_URL}?q=${cityName}&appid=${this.apiKey()}&units=metric&lang=en`
      );
      
      if (!response.ok) {
        if (response.status === 401) {
          throw new Error('Invalid API key. Please check your OpenWeatherMap API key.');
        }
        throw new Error('City not found');
      }
      
      const data = await response.json();
      this.weatherData.set(data);
      
      // Agregar a historial
      if (!this.searchHistory().includes(cityName)) {
        this.searchHistory.update(history => [cityName, ...history.slice(0, 4)]);
      }
    } catch (err) {
      this.error.set(err instanceof Error ? err.message : 'Error getting data');
      this.weatherData.set(null);
    } finally {
      this.loading.set(false);
    }
  }

  handleSearch(event: Event) {
    event.preventDefault();
    if (this.city().trim()) {
      this.fetchWeather(this.city().trim());
    }
  }

  handleHistoryClick(cityName: string) {
    this.city.set(cityName);
    this.fetchWeather(cityName);
  }

  getWeatherIcon(iconCode: string) {
    return `https://openweathermap.org/img/wn/${iconCode}@2x.png`;
  }

  getWeatherDescription(weatherId: number) {
    const descriptions: { [key: number]: string } = {
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
    };
    return descriptions[weatherId] || 'Unknown condition';
  }

  clearApiKey() {
    this.apiKey.set('');
  }

  toggleApiInstructions() {
    this.showApiInstructions.update(value => !value);
  }
}
