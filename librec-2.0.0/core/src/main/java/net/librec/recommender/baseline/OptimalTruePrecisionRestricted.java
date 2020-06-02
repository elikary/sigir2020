
package net.librec.recommender.baseline;

import net.librec.common.LibrecException;
import net.librec.math.structure.SparseVector;
import net.librec.recommender.AbstractRecommender;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.DoubleStream;

/**
 * 
 * @author Rocío Cañamares
 */
public class OptimalTruePrecisionRestricted extends AbstractRecommender {

    private Map<Integer, Double> itemScores;

    @Override
    protected void setup() throws LibrecException {
        super.setup();
        itemScores = new HashMap<>();
    }

    @Override
    protected void trainModel() throws LibrecException {
    }


    @Override
    protected double predict(int userIdx, int itemIdx) throws LibrecException {
        if (!itemScores.containsKey(itemIdx)) {
            SparseVector itemRatingsVectorInTest = testMatrix.column(itemIdx);
            long relTestUsers = DoubleStream.of(itemRatingsVectorInTest.getData()).filter(rating -> rating > 0).count();
            long testUsers = itemRatingsVectorInTest.getCount();
            double score = testUsers == 0 ? 0 : relTestUsers * 1.0/ testUsers;
            itemScores.put(itemIdx, score);
        }

        return itemScores.get(itemIdx);
    }
}
