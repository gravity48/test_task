export const Fetch: typeof useFetch = (request, opts?) => {
    const config = useRuntimeConfig()

    return useFetch(request, { baseURL: config.public.baseURL, ...opts })
}
