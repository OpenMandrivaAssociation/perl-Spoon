%define module	Spoon
%define name	perl-%{module}
%define version 0.24
%define release %mkrel 3
%define _provides_exceptions perl(IO::All)

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A Spiffy Application Building Framework 
URL:		http://search.cpan.org/dist/%{module}
# no available category
Source:     http://search.cpan.org/CPAN/authors/id/I/IN/INGY/%{module}-%{version}.tar.gz
License:	GPL
Group:		Development/Perl
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(IO::All)
BuildRequires:  perl(CGI)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Template)
BuildRequires:  perl(Spiffy)
BuildRequires:  perl(URI::Escape)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Spoon is an Application Framework that is designed primarily for building
Social Software web applications. The Kwiki wiki software is built on top of
Spoon.

Spoon::Base is the primary base class for all the Spoon::* modules. Spoon.pm
inherits from Spiffy.pm.

Spoon is not an application in and of itself. (As compared to Kwiki) You need
to build your own applications from it.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Spoon
%{perl_vendorlib}/Spoon.pm
%{_mandir}/*/*

