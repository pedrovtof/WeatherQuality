import React, { useEffect } from 'react';
import { 
  View, 
  Text, 
  StyleSheet, 
  ScrollView, 
  ActivityIndicator, 
  RefreshControl,
  SafeAreaView,
  TouchableOpacity,
  Dimensions
} from 'react-native';
import { useAppController } from '../controllers/AppController';
import ChartComponent from '../components/ChartComponent';
import { MapPin, Wind, Thermometer, Calendar } from 'lucide-react-native';

const Dashboard: React.FC = () => {
  const { 
    loading, 
    error, 
    location, 
    weatherData, 
    climateData, 
    fetchData,
    availableModels,
    selectedModels,
    toggleModel,
    startDate,
    endDate,
    updateDates
  } = useAppController();

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const adjustDate = (type: 'start' | 'end', days: number) => {
    const current = type === 'start' ? new Date(startDate) : new Date(endDate);
    current.setDate(current.getDate() + days);
    const formatted = current.toISOString().split('T')[0];
    if (type === 'start') {
      updateDates(formatted, endDate);
    } else {
      updateDates(startDate, formatted);
    }
  };

  if (loading && !weatherData) {
    return (
      <View style={styles.centered}>
        <ActivityIndicator size="large" color="#007AFF" />
        <Text style={styles.loadingText}>Fetching your local climate data...</Text>
      </View>
    );
  }

  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView 
        contentContainerStyle={styles.container}
        showsVerticalScrollIndicator={false}
        refreshControl={
          <RefreshControl refreshing={loading} onRefresh={fetchData} color="#007AFF" />
        }
      >
        <View style={styles.header}>
          <Text style={styles.welcome}>WeatherQuality</Text>
          {location && (
            <View style={styles.locationContainer}>
              <MapPin size={14} color="#8E8E93" />
              <Text style={styles.locationText}>
                {location.latitude.toFixed(3)}, {location.longitude.toFixed(3)}
              </Text>
            </View>
          )}
        </View>

        {error && (
          <View style={styles.errorBox}>
            <Text style={styles.errorText}>{error}</Text>
            <TouchableOpacity onPress={fetchData} style={styles.retryButton}>
              <Text style={styles.retryText}>Retry</Text>
            </TouchableOpacity>
          </View>
        )}

        {/* Global Date Filter */}
        <View style={styles.section}>
          <View style={styles.card}>
            <View style={styles.cardHeader}>
              <Calendar size={16} color="#8E8E93" />
              <Text style={styles.cardLabel}>Analysis Period (All Charts)</Text>
            </View>
            
            <View style={styles.dateControls}>
              <View style={styles.dateRow}>
                <View>
                  <Text style={styles.dateTypeLabel}>From</Text>
                  <Text style={styles.dateValue}>{startDate}</Text>
                </View>
                <View style={styles.buttonRow}>
                  <TouchableOpacity onPress={() => adjustDate('start', -7)} style={styles.smallButton}><Text style={styles.smallButtonText}>-7d</Text></TouchableOpacity>
                  <TouchableOpacity onPress={() => adjustDate('start', 7)} style={styles.smallButton}><Text style={styles.smallButtonText}>+7d</Text></TouchableOpacity>
                </View>
              </View>
              
              <View style={[styles.dateRow, { borderTopWidth: 1, borderTopColor: '#F2F2F7', paddingTop: 12, marginTop: 12 }]}>
                <View>
                  <Text style={styles.dateTypeLabel}>To</Text>
                  <Text style={styles.dateValue}>{endDate}</Text>
                </View>
                <View style={styles.buttonRow}>
                  <TouchableOpacity onPress={() => adjustDate('end', -7)} style={styles.smallButton}><Text style={styles.smallButtonText}>-7d</Text></TouchableOpacity>
                  <TouchableOpacity onPress={() => adjustDate('end', 7)} style={styles.smallButton}><Text style={styles.smallButtonText}>+7d</Text></TouchableOpacity>
                </View>
              </View>
            </View>
          </View>
        </View>

        {weatherData && (
          <View style={styles.section}>
            <View style={styles.sectionTitleRow}>
              <Wind size={20} color="#007AFF" />
              <Text style={styles.sectionTitle}>Air Quality (Hourly)</Text>
            </View>
            <ChartComponent 
              title="PM2.5 Levels"
              labels={weatherData.time.map(t => {
                const date = new Date(t);
                const day = date.getDate().toString().padStart(2, '0');
                const month = (date.getMonth() + 1).toString().padStart(2, '0');
                const hours = date.getHours().toString().padStart(2, '0');
                const minutes = date.getMinutes().toString().padStart(2, '0');
                return `${day}/${month} ${hours}:${minutes}`;
              })}
              datasets={[{ data: weatherData.pm2_5 as number[] }]}
              yAxisSuffix=""
            />
            <ChartComponent 
              title="Nitrogen Dioxide"
              labels={weatherData.time.map(t => {
                const date = new Date(t);
                const day = date.getDate().toString().padStart(2, '0');
                const month = (date.getMonth() + 1).toString().padStart(2, '0');
                const hours = date.getHours().toString().padStart(2, '0');
                const minutes = date.getMinutes().toString().padStart(2, '0');
                return `${day}/${month} ${hours}:${minutes}`;
              })}
              datasets={[{ data: weatherData.nitrogen_dioxide as number[], color: () => '#FF9500' }]}
              yAxisSuffix=""
            />
          </View>
        )}

        {climateData && climateData.length > 0 && (
          <View style={styles.section}>
            <View style={styles.sectionTitleRow}>
              <Thermometer size={20} color="#FF3B30" />
              <Text style={styles.sectionTitle}>Climate Trends</Text>
            </View>

            <View style={styles.card}>
               <Text style={[styles.cardLabel, { marginBottom: 12 }]}>Comparison Models</Text>
               <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.chipContainer}>
                {availableModels.map((item) => (
                  <TouchableOpacity
                    key={item.model}
                    style={[
                      styles.filterChip,
                      selectedModels.includes(item.model) && styles.filterChipActive
                    ]}
                    onPress={() => toggleModel(item.model)}
                  >
                    <Text
                      style={[
                        styles.filterChipText,
                        selectedModels.includes(item.model) && styles.filterChipTextActive
                      ]}
                    >
                      {item.model}
                    </Text>
                  </TouchableOpacity>
                ))}
              </ScrollView>
            </View>

            <View style={{ marginTop: 8 }}>
              {climateData.map((data, index) => (
                <ChartComponent 
                  key={data.Model}
                  title={`Max Temp: ${data.Model}`}
                  labels={data.Daily.time.map(t => t.substring(5, 10))}
                  datasets={[{ data: data.Daily.temperature_2m_max as number[], color: () => index === 0 ? '#FF3B30' : '#007AFF' }]}
                  yAxisSuffix="°"
                />
              ))}
            </View>
          </View>
        )}
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#F2F2F7',
  },
  container: {
    paddingHorizontal: 16,
    paddingTop: 24,
    paddingBottom: 40,
  },
  centered: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F2F2F7',
  },
  header: {
    marginBottom: 28,
  },
  welcome: {
    fontSize: 32,
    fontWeight: '800',
    color: '#1C1C1E',
    letterSpacing: -1,
  },
  locationContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 6,
  },
  locationText: {
    marginLeft: 4,
    color: '#8E8E93',
    fontSize: 13,
    fontWeight: '500',
  },
  loadingText: {
    marginTop: 12,
    color: '#8E8E93',
    fontSize: 15,
  },
  section: {
    marginBottom: 32,
  },
  sectionTitleRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 16,
  },
  sectionTitle: {
    fontSize: 22,
    fontWeight: '700',
    marginLeft: 10,
    color: '#1C1C1E',
    letterSpacing: -0.5,
  },
  card: {
    backgroundColor: '#fff',
    borderRadius: 16,
    padding: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 10,
    elevation: 2,
  },
  cardHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 16,
  },
  cardLabel: {
    fontSize: 13,
    fontWeight: '600',
    color: '#8E8E93',
    textTransform: 'uppercase',
    letterSpacing: 0.5,
    marginLeft: 6,
  },
  filterSection: {
    marginBottom: 20,
    flexDirection: 'row',
    alignItems: 'center',
  },
  chipContainer: {
    paddingRight: 10,
  },
  filterChip: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    backgroundColor: '#F2F2F7',
    borderRadius: 20,
    marginRight: 10,
  },
  filterChipActive: {
    backgroundColor: '#007AFF',
  },
  filterChipText: {
    color: '#1C1C1E',
    fontSize: 14,
    fontWeight: '500',
  },
  filterChipTextActive: {
    color: '#fff',
    fontWeight: 'bold',
  },
  dateControls: {
    width: '100%',
  },
  dateRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  dateTypeLabel: {
    fontSize: 12,
    color: '#8E8E93',
    marginBottom: 2,
  },
  dateValue: {
    fontSize: 16,
    fontWeight: '600',
    color: '#1C1C1E',
  },
  buttonRow: {
    flexDirection: 'row',
  },
  smallButton: {
    paddingHorizontal: 12,
    paddingVertical: 8,
    backgroundColor: '#F2F2F7',
    borderRadius: 10,
    marginLeft: 8,
  },
  smallButtonText: {
    fontSize: 13,
    fontWeight: '600',
    color: '#007AFF',
  },
  errorBox: {
    backgroundColor: '#FFE5E5',
    padding: 16,
    borderRadius: 16,
    marginBottom: 24,
    alignItems: 'center',
  },
  errorText: {
    color: '#FF3B30',
    marginBottom: 12,
    textAlign: 'center',
    fontWeight: '500',
  },
  retryButton: {
    backgroundColor: '#FF3B30',
    paddingHorizontal: 24,
    paddingVertical: 10,
    borderRadius: 12,
  },
  retryText: {
    color: '#fff',
    fontWeight: 'bold',
  },
});

export default Dashboard;
