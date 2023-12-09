# # Basic Usage
#
# The LFSIR package provides easy access to Iran's Labor Force Survey data.  
# We can load the raw survey tables and enrich them with additional informations.
#
# ## Loading Survey Data
#
# The `load_table` function loads survey data for a given year.  
# Let's load the data from 1401.

import lfsir
df = lfsir.load_table(years=1401)
df.head()

# We now have the raw survey data for 1401.  
# Next we can enrich this by adding attributes about each household.

# ## Adding Attributes
#
# The `add_attribute` function can append additional attribute columns based on a household ID.
# This allows easy segmentation and analysis by attributes like province and urban/rural status.

df = lfsir.add_attribute(df, "Province")

# We added the province name for each household.

df = lfsir.add_attribute(df, "Urban_Rural")

# Now we also have the urban/rural status.

# Let's confirm that worked by peeking at the data.

df[["ID", "Province", "Urban_Rural"]].head()

# We now have a enriched dataset ready for further analysis and visualization!