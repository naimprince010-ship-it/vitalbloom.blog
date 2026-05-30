type PostImageProps = {
  alt: string;
  className?: string;
  imageUrl: string;
};

export default function PostImage({ alt, className = "", imageUrl }: PostImageProps) {
  if (!imageUrl) {
    return null;
  }

  return <img src={imageUrl} alt={alt} className={className} loading="lazy" />;
}
