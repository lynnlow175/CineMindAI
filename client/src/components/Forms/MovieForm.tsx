'use client';

import { zodResolver } from '@hookform/resolvers/zod';
import { set, useForm } from 'react-hook-form';
import { z } from 'zod';

import { Button } from '@/components/ui/button';
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form';
import { Textarea } from '@/components/ui/textarea';
import { toast } from '@/components/ui/use-toast';
import { useEffect, useState } from 'react';

const movieFormSchema = z.object({
  text: z.string().max(160).min(4),
});

type MovieFormValues = z.infer<typeof movieFormSchema>;

// This can come from your database or API.
const defaultValues: Partial<MovieFormValues> = {
  text: '',
};

export function MovieForm() {
  const form = useForm<MovieFormValues>({
    resolver: zodResolver(movieFormSchema),
    defaultValues,
    mode: 'onChange',
  });

  function onSubmit(data: MovieFormValues) {
    setTextInput(JSON.stringify(data));
    console.log(data);
  }

  const [textInput, setTextInput] = useState<any>();

  const [data, setData] = useState([]);

  useEffect(() => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      // body: JSON.stringify(textInput),
      body: textInput,
    };

    fetch('http://localhost:5000/recommend', requestOptions)
      .then(response => response.json())
      .then(data => {
        setData(data);
        // console.log(data);
      });
  }, [textInput]);

  return (
    <>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
          <FormField
            control={form.control}
            name="text"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Movie Recommendation</FormLabel>
                <FormControl>
                  <Textarea placeholder="" className="resize-none" {...field} />
                </FormControl>
                <FormDescription>The decription of your movie</FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit">Generate Recommendation</Button>
        </form>
      </Form>
      {data &&
        data?.map((members: any) => {
          return <p>{members}</p>;
        })}
    </>
  );
}
