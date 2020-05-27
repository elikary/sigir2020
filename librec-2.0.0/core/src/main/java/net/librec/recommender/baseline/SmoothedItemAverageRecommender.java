
package net.librec.recommender.baseline;

import net.librec.common.LibrecException;
import net.librec.math.structure.SparseVector;
import net.librec.recommender.AbstractRecommender;

import java.util.HashMap;
import java.util.Map;

/**
 * 
 * @author Rocío Cañamares
 */
public class SmoothedItemAverageRecommender extends AbstractRecommender {


    private Map<Integer, Double> itemMeans;
    private double mu;

    @Override
    protected void setup() throws LibrecException {
        super.setup();
        itemMeans = new HashMap<>();
        mu = 1.0;
    }

    @Override
    protected void trainModel() throws LibrecException {
    }


    @Override
    protected double predict(int userIdx, int itemIdx) throws LibrecException {
        if (!itemMeans.containsKey(itemIdx)) {
            SparseVector itemRatingsVector = trainMatrix.column(itemIdx);
            double relTrainUsers = itemRatingsVector.sum();
            long trainUsers = itemRatingsVector.getCount();
            double mean = (relTrainUsers + mu*globalMean) / (trainUsers + mu);
            itemMeans.put(itemIdx, mean);
        }

        return itemMeans.get(itemIdx);
    }
}
