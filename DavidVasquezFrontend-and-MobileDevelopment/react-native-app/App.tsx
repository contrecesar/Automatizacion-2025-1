import React, { useState, useEffect } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  TextInput,
  ScrollView,
  Alert,
  Platform,
  SafeAreaView,
  StatusBar,
} from 'react-native';

export default function App() {
  const [count, setCount] = useState(0);
  const [inputValue, setInputValue] = useState('');
  const [showInfo, setShowInfo] = useState(false);
  const [items, setItems] = useState(['React Native', 'Expo', 'Cross-platform', 'JavaScript']);
  
  // Task Manager states
  const [taskInput, setTaskInput] = useState('');
  const [tasks, setTasks] = useState([
    { id: 1, text: 'Learn React Native', completed: false, priority: 'high' },
    { id: 2, text: 'Build mobile app', completed: true, priority: 'medium' },
    { id: 3, text: 'Deploy to app store', completed: false, priority: 'low' }
  ]);
  const [filter, setFilter] = useState('all'); // all, active, completed

  // useEffect para efectos secundarios
  useEffect(() => {
    console.log(`React Native counter changed to: ${count}`);
  }, [count]);

  const increment = () => setCount((prev: number) => prev + 1);
  const decrement = () => setCount((prev: number) => prev - 1);

  const addItem = () => {
    if (inputValue.trim()) {
      setItems((prev: string[]) => [...prev, inputValue]);
      setInputValue('');
    }
  };

  const removeItem = (index: number) => {
    setItems((prev: string[]) => prev.filter((_: string, i: number) => i !== index));
  };

  // Task Manager functions
  const addTask = () => {
    if (taskInput.trim()) {
      const newTask = {
        id: Date.now(),
        text: taskInput.trim(),
        completed: false,
        priority: 'medium' as const
      };
      setTasks((prev: any[]) => [...prev, newTask]);
      setTaskInput('');
    }
  };

  const toggleTask = (id: number) => {
    setTasks((prev: any[]) => 
      prev.map(task => 
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  const deleteTask = (id: number) => {
    setTasks((prev: any[]) => prev.filter(task => task.id !== id));
  };

  const setTaskPriority = (id: number, priority: string) => {
    setTasks((prev: any[]) => 
      prev.map(task => 
        task.id === id ? { ...task, priority } : task
      )
    );
  };

  const filteredTasks = tasks.filter(task => {
    if (filter === 'active') return !task.completed;
    if (filter === 'completed') return task.completed;
    return true;
  });

  const showPlatformInfo = () => {
    Alert.alert(
      'Platform Information',
      `You are running on: ${Platform.OS}\nVersion: ${Platform.Version}\nIs iOS: ${Platform.OS === 'ios'}\nIs Android: ${Platform.OS === 'android'}`,
      [{ text: 'OK' }]
    );
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="light-content" backgroundColor="#1a1a2e" />
      
      <ScrollView style={styles.scrollView} showsVerticalScrollIndicator={false}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.headerTitle}>🚀 React Native - Cross-Platform</Text>
          <Text style={styles.headerSubtitle}>Educational App demonstrating React Native features</Text>
        </View>



        {/* React Native Info */}
        <View style={styles.infoCard}>
          <Text style={styles.cardTitle}>What is React Native?</Text>
          <View style={styles.infoList}>
            <Text style={styles.infoItem}>📱 Native mobile apps with JavaScript</Text>
            <Text style={styles.infoItem}>🔄 Single codebase for iOS & Android</Text>
            <Text style={styles.infoItem}>⚡ Real native components</Text>
            <Text style={styles.infoItem}>🎯 Built on React principles</Text>
            <Text style={styles.infoItem}>🌐 Cross-platform development</Text>
            <Text style={styles.infoItem}>💪 Community backed by Meta</Text>
          </View>
        </View>

        {/* Counter Feature */}
        <View style={styles.featureCard}>
          <Text style={styles.cardTitle}>🎯 State Management (useState)</Text>
          <Text style={styles.counterText}>Counter: {count}</Text>
          <View style={styles.buttonRow}>
            <TouchableOpacity style={styles.button} onPress={decrement}>
              <Text style={styles.buttonText}>-</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.button} onPress={increment}>
              <Text style={styles.buttonText}>+</Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* Input Feature */}
        <View style={styles.featureCard}>
          <Text style={styles.cardTitle}>📝 Text Input & State</Text>
          <TextInput
            style={styles.textInput}
            value={inputValue}
            onChangeText={setInputValue}
            placeholder="Write something..."
            placeholderTextColor="#666"
          />
          <Text style={styles.inputText}>Text: {inputValue}</Text>
          <TouchableOpacity style={styles.addButton} onPress={addItem}>
            <Text style={styles.addButtonText}>Add Item</Text>
          </TouchableOpacity>
        </View>

        {/* Conditional Rendering */}
        <View style={styles.featureCard}>
          <Text style={styles.cardTitle}>🔄 Conditional Rendering</Text>
          <TouchableOpacity 
            style={styles.toggleButton} 
            onPress={() => setShowInfo(!showInfo)}
          >
            <Text style={styles.toggleButtonText}>
              {showInfo ? 'Hide' : 'Show'} Information
            </Text>
          </TouchableOpacity>
          {showInfo && (
            <View style={styles.infoBox}>
              <Text style={styles.infoBoxText}>
                This text appears/disappears using conditional rendering
              </Text>
              <Text style={styles.infoBoxText}>
                React Native handles state automatically
              </Text>
            </View>
          )}
        </View>

        {/* List Management */}
        <View style={styles.featureCard}>
          <Text style={styles.cardTitle}>📋 List Management</Text>
          {items.map((item, index) => (
            <View key={index} style={styles.listItem}>
              <Text style={styles.listItemText}>{item}</Text>
              <TouchableOpacity 
                style={styles.removeButton}
                onPress={() => removeItem(index)}
              >
                <Text style={styles.removeButtonText}>×</Text>
              </TouchableOpacity>
            </View>
          ))}
        </View>

        {/* Task Manager App */}
        <View style={styles.featureCard}>
          <Text style={styles.cardTitle}>📋 Task Manager App</Text>
          
          {/* Add Task Input */}
          <View style={styles.taskInputContainer}>
            <TextInput
              style={styles.taskInput}
              value={taskInput}
              onChangeText={setTaskInput}
              placeholder="Enter a new task..."
              placeholderTextColor="#666"
            />
            <TouchableOpacity style={styles.addTaskButton} onPress={addTask}>
              <Text style={styles.addTaskButtonText}>Add</Text>
            </TouchableOpacity>
          </View>

          {/* Filter Buttons */}
          <View style={styles.filterContainer}>
            <TouchableOpacity 
              style={[styles.filterButton, filter === 'all' && styles.filterButtonActive]}
              onPress={() => setFilter('all')}
            >
              <Text style={[styles.filterButtonText, filter === 'all' && styles.filterButtonTextActive]}>
                All ({tasks.length})
              </Text>
            </TouchableOpacity>
            <TouchableOpacity 
              style={[styles.filterButton, filter === 'active' && styles.filterButtonActive]}
              onPress={() => setFilter('active')}
            >
              <Text style={[styles.filterButtonText, filter === 'active' && styles.filterButtonTextActive]}>
                Active ({tasks.filter(t => !t.completed).length})
              </Text>
            </TouchableOpacity>
            <TouchableOpacity 
              style={[styles.filterButton, filter === 'completed' && styles.filterButtonActive]}
              onPress={() => setFilter('completed')}
            >
              <Text style={[styles.filterButtonText, filter === 'completed' && styles.filterButtonTextActive]}>
                Completed ({tasks.filter(t => t.completed).length})
              </Text>
            </TouchableOpacity>
          </View>

          {/* Task List */}
          <View style={styles.taskList}>
            {filteredTasks.map((task) => (
              <View key={task.id} style={styles.taskItem}>
                <TouchableOpacity 
                  style={styles.taskCheckbox}
                  onPress={() => toggleTask(task.id)}
                >
                  <Text style={styles.taskCheckboxText}>
                    {task.completed ? '✓' : '○'}
                  </Text>
                </TouchableOpacity>
                
                <View style={styles.taskContent}>
                  <Text style={[
                    styles.taskText, 
                    task.completed && styles.taskTextCompleted
                  ]}>
                    {task.text}
                  </Text>
                  <View style={styles.taskPriority}>
                    <Text style={[
                      styles.priorityText,
                      task.priority === 'high' && styles.priorityHigh,
                      task.priority === 'medium' && styles.priorityMedium,
                      task.priority === 'low' && styles.priorityLow
                    ]}>
                      {task.priority.toUpperCase()}
                    </Text>
                  </View>
                </View>

                <View style={styles.taskActions}>
                  <TouchableOpacity 
                    style={styles.priorityButton}
                    onPress={() => setTaskPriority(task.id, 'high')}
                  >
                    <Text style={[styles.priorityButtonText, task.priority === 'high' && styles.priorityButtonActive]}>H</Text>
                  </TouchableOpacity>
                  <TouchableOpacity 
                    style={styles.priorityButton}
                    onPress={() => setTaskPriority(task.id, 'medium')}
                  >
                    <Text style={[styles.priorityButtonText, task.priority === 'medium' && styles.priorityButtonActive]}>M</Text>
                  </TouchableOpacity>
                  <TouchableOpacity 
                    style={styles.priorityButton}
                    onPress={() => setTaskPriority(task.id, 'low')}
                  >
                    <Text style={[styles.priorityButtonText, task.priority === 'low' && styles.priorityButtonActive]}>L</Text>
                  </TouchableOpacity>
                  <TouchableOpacity 
                    style={styles.deleteTaskButton}
                    onPress={() => deleteTask(task.id)}
                  >
                    <Text style={styles.deleteTaskButtonText}>×</Text>
                  </TouchableOpacity>
                </View>
              </View>
            ))}
          </View>

          {filteredTasks.length === 0 && (
            <Text style={styles.emptyText}>No tasks found</Text>
          )}
        </View>

        {/* Platform Detection */}
        <View style={styles.featureCard}>
          <Text style={styles.cardTitle}>📱 Platform Detection</Text>
          <Text style={styles.platformText}>
            Current Platform: {Platform.OS.toUpperCase()}
          </Text>
          <Text style={styles.platformText}>
            Version: 1.0.0
          </Text>
          <TouchableOpacity style={styles.platformButton} onPress={showPlatformInfo}>
            <Text style={styles.platformButtonText}>Show Platform Info</Text>
          </TouchableOpacity>
        </View>

        {/* React Native vs Web Comparison */}
        <View style={styles.featureCard}>
          <Text style={styles.cardTitle}>🔄 React Native vs Web</Text>
          <View style={styles.comparisonContainer}>
            <View style={styles.comparisonColumn}>
              <Text style={styles.comparisonTitle}>React Web</Text>
              <Text style={styles.comparisonItem}>• HTML elements</Text>
              <Text style={styles.comparisonItem}>• CSS styling</Text>
              <Text style={styles.comparisonItem}>• Browser APIs</Text>
              <Text style={styles.comparisonItem}>• Web-only features</Text>
            </View>
            <View style={styles.comparisonColumn}>
              <Text style={styles.comparisonTitle}>React Native</Text>
              <Text style={styles.comparisonItem}>• Native components</Text>
              <Text style={styles.comparisonItem}>• StyleSheet API</Text>
              <Text style={styles.comparisonItem}>• Device APIs</Text>
              <Text style={styles.comparisonItem}>• Cross-platform</Text>
            </View>
          </View>
        </View>

        {/* Expo Benefits */}
        <View style={styles.featureCard}>
          <Text style={styles.cardTitle}>⚡ Expo Benefits</Text>
          <Text style={styles.expoText}>• Fast development setup</Text>
          <Text style={styles.expoText}>• Over-the-air updates</Text>
          <Text style={styles.expoText}>• Built-in APIs and services</Text>
          <Text style={styles.expoText}>• Easy deployment</Text>
          <Text style={styles.expoText}>• Managed workflow</Text>
        </View>

        {/* Code Example */}
        <View style={styles.featureCard}>
          <Text style={styles.cardTitle}>💻 React Native Code Example</Text>
          <View style={styles.codeContainer}>
            <Text style={styles.codeText}>
{`import React, { useState } from 'react';
import { View, Text, TouchableOpacity } from 'react-native';

export default function App() {
  const [count, setCount] = useState(0);
  
  return (
    <View>
      <Text>Counter: {count}</Text>
      <TouchableOpacity onPress={() => setCount(count + 1)}>
        <Text>Increment</Text>
      </TouchableOpacity>
    </View>
  );
}`}
            </Text>
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1a1a2e',
  },
  scrollView: {
    flex: 1,
    padding: 20,
  },
  header: {
    alignItems: 'center',
    marginBottom: 20,
    paddingVertical: 20,
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#00d4ff',
    textAlign: 'center',
    marginBottom: 8,
  },
  headerSubtitle: {
    fontSize: 16,
    color: '#ffffff',
    textAlign: 'center',
    opacity: 0.8,
  },
  infoCard: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 15,
    padding: 20,
    marginBottom: 20,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.2)',
  },
  featureCard: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 15,
    padding: 20,
    marginBottom: 20,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.2)',
  },
  cardTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#00d4ff',
    marginBottom: 15,
    textAlign: 'center',
  },
  infoList: {
    alignItems: 'center',
  },
  infoItem: {
    fontSize: 18,
    color: '#ffffff',
    marginBottom: 12,
    textAlign: 'center',
    fontWeight: '500',
  },
  counterText: {
    fontSize: 20,
    color: '#ffffff',
    textAlign: 'center',
    marginBottom: 15,
  },
  buttonRow: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: 15,
  },
  button: {
    backgroundColor: '#00d4ff',
    borderRadius: 25,
    width: 50,
    height: 50,
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonText: {
    color: '#ffffff',
    fontSize: 24,
    fontWeight: 'bold',
  },
  textInput: {
    backgroundColor: 'rgba(255, 255, 255, 0.9)',
    borderRadius: 8,
    padding: 12,
    fontSize: 16,
    marginBottom: 10,
    color: '#333',
  },
  inputText: {
    fontSize: 16,
    color: '#ffffff',
    marginBottom: 10,
  },
  addButton: {
    backgroundColor: '#00d4ff',
    borderRadius: 8,
    padding: 12,
    alignItems: 'center',
  },
  addButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  toggleButton: {
    backgroundColor: '#00d4ff',
    borderRadius: 8,
    padding: 12,
    alignItems: 'center',
    marginBottom: 10,
  },
  toggleButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  infoBox: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 8,
    padding: 15,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.2)',
  },
  infoBoxText: {
    color: '#ffffff',
    fontSize: 14,
    marginBottom: 5,
  },
  listItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 8,
    padding: 12,
    marginBottom: 8,
  },
  listItemText: {
    color: '#ffffff',
    fontSize: 16,
    flex: 1,
  },
  removeButton: {
    backgroundColor: '#ff4757',
    borderRadius: 15,
    width: 30,
    height: 30,
    justifyContent: 'center',
    alignItems: 'center',
  },
  removeButtonText: {
    color: '#ffffff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  platformText: {
    color: '#ffffff',
    fontSize: 16,
    marginBottom: 8,
    textAlign: 'center',
  },
  platformButton: {
    backgroundColor: '#00d4ff',
    borderRadius: 8,
    padding: 12,
    alignItems: 'center',
    marginTop: 10,
  },
  platformButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  comparisonContainer: {
    flexDirection: 'row',
    gap: 15,
  },
  comparisonColumn: {
    flex: 1,
    alignItems: 'center',
  },
  comparisonTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#00d4ff',
    marginBottom: 15,
    textAlign: 'center',
  },
  comparisonItem: {
    color: '#ffffff',
    fontSize: 16,
    marginBottom: 8,
    textAlign: 'center',
    fontWeight: '500',
  },
  expoText: {
    color: '#ffffff',
    fontSize: 18,
    marginBottom: 12,
    textAlign: 'center',
    fontWeight: '500',
  },
  codeContainer: {
    backgroundColor: '#1e1e1e',
    borderRadius: 8,
    padding: 15,
    borderWidth: 1,
    borderColor: '#333',
  },
  codeText: {
    color: '#d4d4d4',
    fontSize: 12,
    fontFamily: Platform.OS === 'ios' ? 'Menlo' : 'monospace',
    lineHeight: 18,
  },
  // Task Manager styles
  taskInputContainer: {
    flexDirection: 'row',
    marginBottom: 15,
    gap: 10,
  },
  taskInput: {
    flex: 1,
    backgroundColor: 'rgba(255, 255, 255, 0.9)',
    borderRadius: 8,
    padding: 12,
    fontSize: 16,
    color: '#333',
  },
  addTaskButton: {
    backgroundColor: '#00d4ff',
    borderRadius: 8,
    padding: 12,
    justifyContent: 'center',
    alignItems: 'center',
    minWidth: 60,
  },
  addTaskButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  filterContainer: {
    flexDirection: 'row',
    marginBottom: 15,
    gap: 8,
  },
  filterButton: {
    flex: 1,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 8,
    padding: 10,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.2)',
  },
  filterButtonActive: {
    backgroundColor: '#00d4ff',
    borderColor: '#00d4ff',
  },
  filterButtonText: {
    color: '#ffffff',
    fontSize: 12,
    fontWeight: '600',
  },
  filterButtonTextActive: {
    color: '#ffffff',
    fontWeight: 'bold',
  },
  taskList: {
    marginBottom: 10,
  },
  taskItem: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 8,
    padding: 12,
    marginBottom: 8,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.2)',
  },
  taskCheckbox: {
    width: 30,
    height: 30,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  taskCheckboxText: {
    fontSize: 20,
    color: '#00d4ff',
    fontWeight: 'bold',
  },
  taskContent: {
    flex: 1,
  },
  taskText: {
    color: '#ffffff',
    fontSize: 16,
    marginBottom: 4,
  },
  taskTextCompleted: {
    textDecorationLine: 'line-through',
    opacity: 0.6,
  },
  taskPriority: {
    marginTop: 4,
  },
  priorityText: {
    fontSize: 10,
    fontWeight: 'bold',
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 4,
    overflow: 'hidden',
  },
  priorityHigh: {
    backgroundColor: '#ff4757',
    color: '#ffffff',
  },
  priorityMedium: {
    backgroundColor: '#ffa502',
    color: '#ffffff',
  },
  priorityLow: {
    backgroundColor: '#2ed573',
    color: '#ffffff',
  },
  taskActions: {
    flexDirection: 'row',
    gap: 4,
  },
  priorityButton: {
    width: 24,
    height: 24,
    borderRadius: 12,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  priorityButtonText: {
    color: '#ffffff',
    fontSize: 12,
    fontWeight: 'bold',
  },
  priorityButtonActive: {
    backgroundColor: '#00d4ff',
  },
  deleteTaskButton: {
    width: 24,
    height: 24,
    borderRadius: 12,
    backgroundColor: '#ff4757',
    justifyContent: 'center',
    alignItems: 'center',
  },
  deleteTaskButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  emptyText: {
    color: '#ffffff',
    fontSize: 16,
    textAlign: 'center',
    opacity: 0.6,
    fontStyle: 'italic',
  },
});
