<script>
  import { onMount } from 'svelte';

  let data = null;
  let formInputs = {};
  let isLoading = true;
  let error = null;

  const API = 'http://127.0.0.1:8000';

  const fetchData = async () => {
    try {
      const response = await fetch(API);
      if (response.ok) {
        data = await response.json();
        initializeFormInputs(data);
      } else {
        throw new Error('Failed to fetch data');
      }
    } catch (err) {
      error = err.message;
    } finally {
      isLoading = false;
    }
  };

  const initializeFormInputs = (data) => {
    for (const category of Object.keys(data)) {
      data[category].forEach(item => {
        formInputs[item.name] = '';
      });
    }
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch(API, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formInputs),
      });

      if (response.ok) {
        // Successful submission handling logic here
        console.log('Data successfully submitted to the API');
      } else {
        throw new Error('Failed to submit data to the API');
      }
    } catch (err) {
      console.error(err);
      // Handle error on submission failure
    }
  };

  onMount(() => {
    fetchData();
  });

</script>

<main>
  {#if isLoading}
    <p>Loading...</p>
  {:else if error}
    <p>Error: {error}</p>
  {:else}
    <pre>{JSON.stringify(data, null, 2)}</pre>
    <form on:submit|preventDefault={handleSubmit}>
      {#each Object.keys(data) as category}
        <h3>{category}</h3>
        {#each data[category] as item}
          <div class="form-group">
            <label for={item.name}>{item.name}</label>
            <input type="text" id={item.name} bind:value={formInputs[item.name]} />
          </div>
        {/each}
      {/each}
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  {/if}
</main>

<style>
  /* Your styles here */
  .form-group {
    margin-bottom: 1rem;
  }
</style>
