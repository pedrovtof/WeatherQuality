import React from 'react';
import Dashboard from './src/views/Dashboard';
import { StatusBar } from 'expo-status-bar';

export default function App() {
  return (
    <>
      <StatusBar style="auto" />
      <Dashboard />
    </>
  );
}
