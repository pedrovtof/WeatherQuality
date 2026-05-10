import React from 'react';
import { View, Text, StyleSheet, Dimensions } from 'react-native';
import { LineChart } from 'react-native-chart-kit';

interface ChartProps {
  title: string;
  labels: string[];
  datasets: { data: number[]; color?: (opacity: number) => string }[];
  yAxisSuffix?: string;
}

const ChartComponent: React.FC<ChartProps> = ({ title, labels, datasets, yAxisSuffix = "" }) => {
  // Get screen width and subtract padding for safety
  const screenWidth = Dimensions.get('window').width;
  // Dashboard has padding: 20, and ChartComponent container has marginHorizontal via Dashboard's padding
  // We subtract Dashboard padding (20*2) + ChartComponent container internal padding (10*2)
  const chartWidth = screenWidth - 60; 

  // Limit labels for readability - show about 5-6 max
  const skip = Math.max(1, Math.floor(labels.length / 5));
  const displayLabels = labels.filter((_, i) => i % skip === 0).slice(0, 6);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{title}</Text>
      <View style={styles.chartWrapper}>
        <LineChart
          data={{
            labels: displayLabels,
            datasets: datasets,
          }}
          width={chartWidth}
          height={200}
          yAxisSuffix={yAxisSuffix}
          chartConfig={{
            backgroundColor: '#ffffff',
            backgroundGradientFrom: '#ffffff',
            backgroundGradientTo: '#ffffff',
            decimalPlaces: 1,
            color: (opacity = 1) => `rgba(0, 122, 255, ${opacity})`,
            labelColor: (opacity = 1) => `rgba(100, 100, 100, ${opacity})`,
            style: {
              borderRadius: 16,
            },
            propsForDots: {
              r: '3',
              strokeWidth: '1',
              stroke: '#007AFF',
            },
            propsForLabels: {
              fontSize: 10,
            }
          }}
          bezier
          style={styles.chart}
          withInnerLines={false}
          withOuterLines={true}
          withVerticalLines={false}
          withHorizontalLines={true}
          fromZero={true}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginVertical: 12,
    padding: 12,
    backgroundColor: '#fff',
    borderRadius: 16,
    // iOS Shadow
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.05,
    shadowRadius: 8,
    // Android Elevation
    elevation: 4,
    width: '100%',
  },
  chartWrapper: {
    alignItems: 'center',
    justifyContent: 'center',
    overflow: 'hidden',
  },
  title: {
    fontSize: 15,
    fontWeight: '600',
    marginBottom: 12,
    color: '#1C1C1E',
    letterSpacing: -0.3,
  },
  chart: {
    marginVertical: 8,
    borderRadius: 16,
    paddingRight: 40, // Ensure enough room for Y axis labels
  },
});

export default ChartComponent;
