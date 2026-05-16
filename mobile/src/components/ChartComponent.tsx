import React from 'react';
import { View, Text, StyleSheet, Dimensions, ScrollView } from 'react-native';
import { LineChart } from 'react-native-chart-kit';

interface ChartProps {
  title: string;
  labels: string[];
  datasets: { data: number[]; color?: (opacity: number) => string }[];
  yAxisSuffix?: string;
}

const ChartComponent: React.FC<ChartProps> = ({ title, labels, datasets, yAxisSuffix = "" }) => {
  const screenWidth = Dimensions.get('window').width;
  // Dashboard has padding: 16. Parent container has padding: 12.
  const containerPadding = 16 * 2 + 12 * 2;
  const availableWidth = screenWidth - containerPadding;

  // Calculate dynamic width: at least the screen width, but expands with labels
  // 60 pixels per label seems reasonable for "DD/MM HH:mm"
  const dynamicWidth = Math.max(availableWidth, labels.length * 60);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{title}</Text>
      <ScrollView horizontal showsHorizontalScrollIndicator={true} style={styles.scrollView}>
        <LineChart
          data={{
            labels: labels,
            datasets: datasets,
          }}
          width={dynamicWidth}
          height={260}
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
          withVerticalLines={true}
          withHorizontalLines={true}
          fromZero={true}
          verticalLabelRotation={30}
        />
      </ScrollView>
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
  scrollView: {
    borderRadius: 16,
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
    paddingRight: 40,
    paddingBottom: 20,
  },
});

export default ChartComponent;
